# Baymax Eyes 👀

**Gentle face-tracking animated eyes inspired by Disney's Big Hero 6**

Create a caring digital companion that watches over you while you work. Baymax Eyes uses real-time face detection to animate gentle eyes that smoothly follow your movements and blink naturally on your desktop.

![Baymax GIF](baymax.gif)

## Features

- **Real-time Face Tracking**: Smooth eye movement that follows your face position
- **Natural Blinking Animation**: Time-based blinking with realistic eyelid movement
- **Anti-Jitter Technology**: Intelligent movement threshold to eliminate camera noise
- **Fullscreen Experience**: Immersive desktop companion mode
- **Sound Effects**: Subtle audio feedback during blink animations
- **Modular Design**: Clean separation between face detection and animation systems

## Demo

*Ever wanted Baymax's gentle eyes watching over you while you work? This project creates animated eyes on your desktop that smoothly track your face movements and blink naturally, like having a caring digital companion. The eyes follow you around your screen with Disney-level charm, providing that perfect mix of comfort and wonder while you code or work.*

## Quick Start

### Prerequisites

- Python 3.8+
- Webcam
- Windows/macOS/Linux

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/baymax-eyes.git
cd baymax-eyes
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python animation.py
```

## Usage

### Basic Usage

Run the main animation:
```bash
python animation.py
```

- **ESC**: Exit fullscreen mode
- **Space**: Pause/Resume tracking (if implemented)
- **Q**: Quit application

### Face Tracker Module

The face tracking functionality is modularized in the `facetracker_module`:

```python
from facetracker_module.facetracker import Tracker

# Initialize tracker
tracker = Tracker(
    cam_id=0,
    model_asset_path='blazeface_sr.tflite',
    operation=your_callback_function
)

# Start tracking
tracker.start(looping_condition=True)
```

### Customization

#### Blink Timing
Modify blink frequency and duration in `animation.py`:
```python
blink(prevTime, 5, 1, toplid, bottomlid)  # Blink every 5 seconds, 1 second duration
```

#### Eye Positioning
Adjust eye spacing and position:
```python
gap = 300  # Distance between pupils
pupil1.x = centre_x + gap  # Right eye
pupil2.x = centre_x - gap  # Left eye
```

#### Movement Sensitivity
Change the anti-jitter threshold:
```python
if abs(x - prev_x) > 10:  # Adjust threshold value
```

## Technical Details

### Architecture

The project uses a multi-threaded architecture:

- **Main Thread**: Handles Pygame animation loop and user interface
- **Face Tracking Thread**: Runs MediaPipe face detection in background
- **Global State**: Shared variables for pupil positions and blink states

### Face Detection

- **Model**: MediaPipe BlazeFace (short-range)
- **Mode**: LIVE_STREAM with callback-based processing
- **Input**: Webcam feed at default resolution
- **Output**: Bounding box coordinates for face position

### Animation System

- **Framework**: Pygame for real-time graphics
- **Rendering**: Vector-based eye drawing with dynamic positioning
- **Blinking**: State machine with smooth eyelid animation
- **Audio**: Pygame mixer for blink sound effects

### Anti-Jitter Algorithm

Implements movement threshold filtering to prevent camera noise from causing eye twitching:

```python
if abs(x - prev_x) > threshold:
    # Update eye positions
    update_pupil_positions()
```

## Configuration

### Camera Settings

Modify camera input in `facetracker.py`:
```python
self.cap = cv2.VideoCapture(cam_id)  # Change cam_id for different cameras
```

### Display Settings

Fullscreen mode is default. To run in windowed mode, modify `animation.py`:
```python
screen = pygame.display.set_mode((1200, 800))  # Replace FULLSCREEN with dimensions
```

### Sound Effects

Multiple blink sound options are provided:
- `pop-amp.mp3` - Default pop sound
- `blink-amp.mp3` - Subtle blink sound
- `cheerful-blink.mp3` - Upbeat blink sound

Change sound in `animation.py`:
```python
mixer.music.load('your-sound-file.mp3')
```

## Performance

- **CPU Usage**: Moderate (face detection is computationally intensive)
- **Memory Usage**: Low (~50-100MB depending on camera resolution)
- **Frame Rate**: 30+ FPS for smooth animation
- **Latency**: <100ms face tracking response time

## Troubleshooting

### Common Issues

**Camera not detected:**
- Ensure webcam is connected and not in use by other applications
- Try different `cam_id` values (0, 1, 2, etc.)

**Poor face tracking:**
- Ensure good lighting conditions
- Position yourself clearly in front of the camera
- Adjust the movement threshold if eyes are too sensitive/insensitive

**Performance issues:**
- Close other resource-intensive applications
- Reduce camera resolution in `facetracker.py`
- Consider using a more powerful computer for real-time processing

**Audio not working:**
- Check system audio settings
- Ensure audio files are in the correct directory
- Verify Pygame mixer initialization

## Development

### Adding New Features

The modular design makes it easy to extend functionality:

1. **New Animations**: Add to the main animation loop in `animation.py`
2. **Enhanced Tracking**: Modify the callback function in `move_pupil()`
3. **UI Elements**: Add Pygame UI components to the main loop
4. **Sound Effects**: Add new audio files and modify the blink function

### Testing

Test the face tracker module independently:
```bash
cd facetracker_module
python example.py
```

## Acknowledgments

- **Disney's Big Hero 6** for the original Baymax character inspiration
- **MediaPipe** for robust face detection capabilities
- **Pygame** for smooth real-time animation framework
- **OpenCV** for computer vision utilities

## Roadmap

- [ ] Voice interaction capabilities
- [ ] Emotional expressions through eye movement patterns
- [ ] Healthcare reminder features
- [ ] Multiple eye designs and themes
- [ ] Gesture recognition integration
- [ ] Mobile app version

---

*"I am Baymax, your personal healthcare companion." - Now available for your desktop.*