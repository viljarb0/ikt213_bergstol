import cv2
import numpy as np

def align_images(image_to_align, reference_image, max_features=1500, good_match_percent=0.15, aligned_path="aligned.png", matches_path="matches.png"):
    ref = cv2.imread(reference_image)
    mov = cv2.imread(image_to_align)
    if ref is None or mov is None:
        print("Could not open or find the images.")
        return

    gray_ref = cv2.cvtColor(ref, cv2.COLOR_BGR2GRAY)
    gray_mov = cv2.cvtColor(mov, cv2.COLOR_BGR2GRAY)

    orb = cv2.ORB_create(nfeatures=max_features)
    kp_ref, des_ref = orb.detectAndCompute(gray_ref, None)
    kp_mov, des_mov = orb.detectAndCompute(gray_mov, None)
    if des_ref is None or des_mov is None or len(kp_ref) < 4 or len(kp_mov) < 4:
        return

    bf = cv2.BFMatcher(cv2.NORM_HAMMING)
    knn = bf.knnMatch(des_mov, des_ref, k=2)

    good = []
    for pair in knn:
        if len(pair) == 2:
            m, n = pair
            if m.distance < 0.75 * n.distance:
                good.append(m)
    if len(good) < 4:
        return

    matches = sorted(good, key=lambda x: x.distance, reverse=False)
    if not matches:
        return

    target_keep = max(10, int(len(knn) * good_match_percent))
    keep = min(len(matches), target_keep)
    matches = matches[:keep]

    pts_mov = np.float32([kp_mov[m.queryIdx].pt for m in matches])
    pts_ref = np.float32([kp_ref[m.trainIdx].pt for m in matches])
    H, mask = cv2.findHomography(pts_mov, pts_ref, cv2.RANSAC, 5.0)
    if H is None:
        return

    h, w = ref.shape[:2]
    aligned = cv2.warpPerspective(mov, H, (w, h))

    cv2.imwrite(aligned_path, aligned)
    mask_list = mask.ravel().tolist() if mask is not None else None
    vis = cv2.drawMatches(
        mov, kp_mov, ref, kp_ref, matches, None,
        matchColor=(0, 255, 0),
        matchesMask=mask_list,
        flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS,
    )
    cv2.imwrite(matches_path, vis)


if __name__ == "__main__":
    align_images(
        "align_this.jpg",
        "reference_img.png",
        max_features=1500,
        good_match_percent=0.15
    )
