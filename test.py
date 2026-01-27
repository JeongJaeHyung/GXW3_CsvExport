import winapps

app_list = [
    "GX Works2",
    "GX Works3"
]

# 설치된 모든 앱 리스트 출력
for app in winapps.list_installed():
    if app.name in app_list:
        print(f"Found {app.name}")
