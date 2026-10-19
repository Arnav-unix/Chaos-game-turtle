This is a Python script that uses turtle graphics to draw fractals using the chaos game,
This may help you understand it better
https://youtube.com/shorts/QK2SJo-AxT4?si=HJIofUbrQpiR5QcL

# Download

**Linux, Android (Termux), Ios (Ish shell)**

Download the latest file from Releases named "main", 
Navigate to the directory you downloaded the file and 
run this
```bash
./main
```

**Windows, MacOS**

Scroll to the bottom

# Usage
You can leave almost everything as it is but you can change these

**sierpinski triangle**<br>
sides = 3<br>
operation = distance / 2

**pentagon**<br>
sides = 5<br>
operation = distance * 0.618

**hexagon**<br>
sides = 6<br>
operation = distance * (1/3)

You can search more on the internet.


# Windows, MacOS
Because neither i have a Windows nor a MacOS only android, i couldn't make it for Windows or MacOS, but you still can use it like this assuming you have python3 and git installed

Note: These are not tested so please don't ask me if it fails

**Windows, MacOS**

```bash
git clone https://github.com/Arnav-unix/Chaos-game-turtle.git
cd Chaos-game-turtle
python3 main.py
```

If you want a .exe or a MacOS executable file do this

```bash
# Installing pyinstaller
pip3 install pyinstaller

# Assuming you have cloned the repo and are inside it
pyinstaller main.py --clean --onefile --noconsole
```

Now to run it
**Windows**
```bash
.\dist\main.exe
```

**MacOS**
```bash
./dist/main
```
