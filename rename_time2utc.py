import os
from datetime import datetime

def rename_images_with_timestamp(directory_path):
    # 디렉토리에서 파일 목록을 가져오기
    source_directory = os.path.join(os.getcwd(), directory_path)
    file_list = [filename for filename in os.listdir(source_directory) if os.path.isfile(os.path.join(source_directory, filename))]

    # 파일들을 타임스탬프로 변경하여 저장
    file_list.sort()
    for filename in file_list:
        # 현재 파일의 경로 설정
        source_path = os.path.join(source_directory, filename)
        timestamp = os.path.getmtime(source_path)
        dt_object = datetime.utcfromtimestamp(timestamp)
        microsecond_part = dt_object.strftime("%f")  # 마이크로초까지 포함 (소수점 이하 3자리까지)
        new_filename = f"{int(timestamp)}.{microsecond_part}.jpg"
        new_path = os.path.join(source_directory, new_filename)

        # 파일 이름 변경 (덮어쓰기)
        os.rename(source_path, new_path)

    print('rgb 파일들의 이름이 변경되었습니다.')

# # 함수 호출 (rgb_test 디렉토리의 파일명을 변경하여 덮어쓰기)
# rename_images_with_timestamp('rgb_test')
