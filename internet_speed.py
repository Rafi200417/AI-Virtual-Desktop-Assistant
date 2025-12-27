import speedtest
import time

def check_speed():
    try:
        print("Initializing speed test...")
        wifi = speedtest.Speedtest()

        print("Getting best server...")
        wifi.get_best_server()  # This is important
        time.sleep(1)  # short delay to stabilize

        print("Testing download speed...")
        download = wifi.download()
        time.sleep(1)

        print("Testing upload speed...")
        upload = wifi.upload()

        if download is None or upload is None or download == 0 or upload == 0:
            raise ValueError("Download or Upload returned None or zero")

        download_mbps = download / 1_000_000
        upload_mbps = upload / 1_000_000

        print(f"Download Speed: {download_mbps:.2f} Mbps")
        print(f"Upload Speed: {upload_mbps:.2f} Mbps")

        speedtest.speak(f"Your download speed is {download_mbps:.2f} megabits per second.")
        speedtest.speak(f"Your upload speed is {upload_mbps:.2f} megabits per second.")

    except Exception as e:
        print(f"[ERROR] Internet speed test failed: {e}")
        speedtest.speak("Sorry, I couldn't fetch the internet speed.")
