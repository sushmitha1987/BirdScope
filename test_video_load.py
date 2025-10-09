import cv2

cap = cv2.VideoCapture("D:/BirdSpecies/input/inference_videos/test_video.mp4")

if not cap.isOpened():
    print("❌ Failed to open video.")
else:
    ret, frame = cap.read()
    print("✅ Frame read:", ret)
    if ret:
        print("Frame size:", frame.shape)
    else:
        print("⚠️ No frame could be read. Possibly corrupted video.")

cap.release()
