import cv2
import mediapipe as mp

mp_face_mesh = mp.solutions.face_mesh

def extract_landmarks_mediapipe(image):
    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    with mp_face_mesh.FaceMesh(
        static_image_mode=True,
        max_num_faces=1,
        refine_landmarks=True,
        min_detection_confidence=0.5
    ) as face_mesh:
        results = face_mesh.process(rgb)
        if not results.multi_face_landmarks:
            raise ValueError("No face detected!")

        landmarks = results.multi_face_landmarks[0]
        h, w = image.shape[:2]

        # 정규화된 좌표 → 이미지 좌표로 변환
        points = []
        for lm in landmarks.landmark:
            x = int(lm.x * w)
            y = int(lm.y * h)
            points.append((x, y))

        return points  # (468개 좌표)
