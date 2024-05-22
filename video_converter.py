import subprocess
import pathlib
import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox

def convert_video(input_video_path, output_file_path, output_type):
    if output_type == 'MP4':
        command = f"ffmpeg -i \"{input_video_path}\" -c:v copy -c:a aac \"{output_file_path}\""
    elif output_type == 'MP3':
        command = f"ffmpeg -i \"{input_video_path}\" -vn -ar 44100 -ac 2 -b:a 192k \"{output_file_path}\""
    subprocess.call(command, shell=True)

def select_file_and_convert():
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    
    # Open a file dialog to select the video file
    video_file_path = filedialog.askopenfilename(
        title="Select a video file", 
        filetypes=[("Video files", "*.webm *.mp4 *.mkv *.avi")]
    )
    
    if video_file_path:
        # Ask the user to choose the output type
        output_type = simpledialog.askstring("Output Type", "Enter output type (MP3 or MP4):")
        if output_type.upper() not in ['MP3', 'MP4']:
            messagebox.showerror("Invalid Input", "Please enter a valid output type (MP3 or MP4).")
            return
        
        # Open a save file dialog to specify the output file name
        output_extension = ".mp4" if output_type == 'MP4' else ".mp3"
        output_file_path = filedialog.asksaveasfilename(
            title="Save as", 
            defaultextension=output_extension,
            filetypes=[(f"{output_type} files", f"*{output_extension}")]
        )
        
        if output_file_path:
            convert_video(video_file_path, output_file_path, output_type)
            print(f"Conversion complete. Output file: {output_file_path}")

if __name__ == "__main__":
    select_file_and_convert()
