import cv2
import numpy as np


def align_images(image_to_align, reference_image, max_features, good_match_precent):
    """
    Align image_to_align to reference_image using SIFT keypoints and FLANN matching
    Params:
        image_to_align : str
            Path to the image that should be aligned.
        reference_image : str
            Path to the reference image (alignment target).
        max_features : int
            Maximum number of SIFT features to detect.
        good_match_precent : float
            Lowe's ratio test threshold (0-1) to keep good matches.
    """
    img1_color = cv2.imread(image_to_align)
    img2_color = cv2.imread(reference_image)

    if img1_color is None:
        raise FileNotFoundError(f"Could not read image to align at '{image_to_align}'.")
    if img2_color is None:
        raise FileNotFoundError(f"Could not read reference image at '{reference_image}'.")

    img1_gray = cv2.cvtColor(img1_color, cv2.COLOR_BGR2GRAY)
    img2_gray = cv2.cvtColor(img2_color, cv2.COLOR_BGR2GRAY)

    sift = cv2.SIFT_create(nfeatures=max_features)
    keypoints1, descriptors1 = sift.detectAndCompute(img1_gray, None)
    keypoints2, descriptors2 = sift.detectAndCompute(img2_gray, None)

    if descriptors1 is None or descriptors2 is None or len(keypoints1) == 0 or len(keypoints2) == 0:
        raise RuntimeError("Failed to detect SIFT features in one or both images.")

    print(f"Detected {len(keypoints1)} keypoints in align_this.jpg and {len(keypoints2)} in reference_img.png.")

    flann_index_kdtree = 1
    index_params = dict(algorithm=flann_index_kdtree, trees=5)
    search_params = dict(checks=50)
    flann = cv2.FlannBasedMatcher(index_params, search_params)

    knn_matches = flann.knnMatch(descriptors1, descriptors2, k=2)

    good_matches = []
    for pair in knn_matches:
        if len(pair) == 2 and pair[0].distance < 0.7 * pair[1].distance:
            good_matches.append(pair[0])

    if len(good_matches) < 4:
        one_to_one_matches = [pair[0] for pair in knn_matches if len(pair) > 0]
        if not one_to_one_matches:
            raise RuntimeError("Could not obtain any matches between the images.")

        one_to_one_matches = sorted(one_to_one_matches, key=lambda m: m.distance)
        keep_count = max(4, int(len(one_to_one_matches) * good_match_precent))
        good_matches = one_to_one_matches[:keep_count]

    if len(good_matches) < 4:
        raise RuntimeError(f"Not enough matches ({len(good_matches)}) to compute homography.")

    print(f"Using {len(good_matches)} matches for homography estimation.")

    src_pts = np.float32([keypoints1[m.queryIdx].pt for m in good_matches]).reshape(-1, 1, 2)
    dst_pts = np.float32([keypoints2[m.trainIdx].pt for m in good_matches]).reshape(-1, 1, 2)

    homography, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)
    if homography is None:
        homography, mask = cv2.findHomography(src_pts, dst_pts, 0)

    if homography is None:
        raise RuntimeError("Homography computation failed.")

    height, width = img2_color.shape[:2]
    aligned_image = cv2.warpPerspective(img1_color, homography, (width, height))

    matches_mask = mask.ravel().tolist() if mask is not None else None
    match_vis = cv2.drawMatches(
        img1_color,
        keypoints1,
        img2_color,
        keypoints2,
        good_matches,
        None,
        matchesMask=matches_mask,
        flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS,
    )

    cv2.imwrite("aligned.jpg", aligned_image)
    cv2.imwrite("matches.jpg", match_vis)

    return aligned_image, match_vis


if __name__ == "__main__":
    align_images(
        image_to_align="align_this.jpg",
        reference_image="reference_img-1.png",
        max_features=10,
        good_match_precent=0.7,
    )

