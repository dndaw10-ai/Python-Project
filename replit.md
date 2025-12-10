# Graphics Drawing Application

## Overview
A Python GUI application that demonstrates simple graphics drawing using the graphics.py library (John Zelle's graphics library for educational purposes).

## Project Structure
- `main.py` - Main application file with graphics drawing
- `graphics.py` - Graphics library providing GUI components (GraphWin, Text, Entry, Rectangle, Line, etc.)
- Runs with Python 3.11 and tkinter backend

## Current Program: House Drawing
The program draws a simple house:
- Rectangle for the house body
- Two lines forming a triangular roof
- Click anywhere to close the window

## Architecture
- **Graphics Library**: Custom tkinter wrapper providing simple graphics primitives
- **Coordinate System**: Uses custom coordinate transformation (0-3 horizontal, 0-4 vertical)
- **Event Handling**: Mouse click-based interaction via getMouse() method
- **Drawing Objects**: Rectangle, Line, Point, Circle, Oval, Polygon, Text, Entry

## Recent Changes
- 2025-11-24: User updated program to draw a simple house
- 2025-11-24: Initial setup with graphics.py library and Celsius converter
- Configured VNC workflow for GUI display
- Added Python 3.11 support
