import cv2
import os

def process_video(video_path, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    cap = cv2.VideoCapture(video_path)
    
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    current_frame = 0
    saved_count = 0

    while True:
        cap.set(cv2.CAP_PROP_POS_FRAMES, current_frame)
        ret, frame = cap.read()
        
        if not ret:
            print("End of video or error reading frame.")
            break

        cv2.imshow('Frame', frame)
        cv2.putText(frame, f'Frame: {current_frame+1}/{total_frames}', (10, 30), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        cv2.imshow('Frame', frame)

        key = cv2.waitKey(0) & 0xFF

        if key == ord('s'):
            saved_count += 1
            output_path = os.path.join(output_folder, f'frame_{current_frame+1:04d}.jpg')
            cv2.imwrite(output_path, frame)
            print(f"Saved frame {current_frame+1} as {output_path}")
        elif key == ord('a') and current_frame > 0:
            current_frame -= 1
        elif key == ord('d') and current_frame < total_frames - 1:
            current_frame += 1
        elif key == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

    print(f"Total frames: {total_frames}")
    print(f"Saved frames: {saved_count}")

# 使用示例
video_path = 'path/to/your/video.mp4'
output_folder = 'path/to/output/folder'
process_video(video_path, output_folder)
