from yt_dlp import YoutubeDL

def download_playlist():
    # yt-dlp 옵션 설정
    ydl_opts = {
        'cookiefile': "../.store/.secret/www.youtube.com_cookies.txt",  # Netscape 형식 쿠키 파일 경로
        'format': 'bestvideo[height<=1080]+bestaudio/best[height<=1080]',  # 1080p 화질 선택
        'outtmpl': 'D:\\차트무당\\멤버\\%(upload_date)s_%(title)s.%(ext)s',  # 저장할 파일 이름 형식
        'merge_output_format': 'mp4',  # 영상과 음성 결합 형식
        'download_archive': '../.store/data/chart_shaman_archive.txt'  # 이미 다운로드한 파일 목록 기록
        # 'verbose': True  # 디버깅 정보 출력
    }

    # 다운로드 실행 (재생목록 전체 다운로드)
    playlist_url = 'https://www.youtube.com/playlist?list=PLSFqeN8d8v1xd2jOlz-tu7eCc_3UUuZYO'  # 재생목록 URL
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([playlist_url])

if __name__ == "__main__":
    download_playlist()