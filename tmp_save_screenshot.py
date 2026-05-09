import base64
from pathlib import Path
src = Path(r'c:/Users/hp/AppData/Roaming/Code/User/workspaceStorage/9b22912badffc3bcf1e4a52f09e6620b/GitHub.copilot-chat/chat-session-resources/50ed055d-cbda-4219-9ff5-484399538704/call_RzdVHehMWP7CCeY8Il2336pY__vscode-1777620329463/content.txt')
dst = Path('frontend/public/dashboard.png')
dst.parent.mkdir(parents=True, exist_ok=True)
data = src.read_text()
dst.write_bytes(base64.b64decode(data))
print(dst.resolve())
