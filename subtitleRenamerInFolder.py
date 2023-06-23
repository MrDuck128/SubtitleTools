import os, re

path = os.getcwd()

videos = {}
subtitles = {}

for file in os.listdir(path):
    if os.path.isdir(os.path.join(path, file)) or file[-3:] in ('.py', 'txt', 'exe'):
        continue

    episode = re.findall('[sS]\d+[eE]\d+', file)[0].upper()

    if file[-3:] in ('mkv', 'mp4', 'mov', 'avi'):
        videos[episode] = file[:-4]
    else:
        subtitles[episode] = file


renamingScheme = []
for episode in videos:
  if episode in videos and episode in subtitles:
    if videos[episode] != subtitles[episode][:-4]:
        renamingScheme.append((videos[episode], subtitles[episode]))

for (video, subtitle) in renamingScheme:
    os.rename(os.path.join(path, subtitle), os.path.join(path, video + subtitle[-4:]))
