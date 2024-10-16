import { HttpClient } from '@angular/common/http';
import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  text: string = '';
  voice: string = 'en';
  files: string[] = [];
  audioSrc: string | null = null;
  isRecording: boolean = false;
  mediaRecorder: MediaRecorder | null = null;
  audioChunks: Blob[] = [];

  constructor(private http: HttpClient) {}

  ngOnInit() {
    this.getFiles();
  }

  convertTextToSpeech() {
    this.http.post('http://localhost:5000/api/convert', { text: this.text, voice: this.voice })
      .subscribe(
        (response: any) => {
          if (response.success) {
            this.getFiles();
            alert('Conversion successful!');
          }
        },
        error => console.error('Error:', error)
      );
  }

  getFiles() {
    this.http.get('http://localhost:5000/api/files')
      .subscribe(
        (response: any) => {
          this.files = response.files;
        },
        error => console.error('Error:', error)
      );
  }

  playFile(filename: string) {
    this.audioSrc = `http://localhost:5000/api/files/${filename}`;
  }

  deleteFile(filename: string) {
    this.http.delete(`http://localhost:5000/api/files/${filename}`)
      .subscribe(
        () => {
          this.getFiles();
          alert('File deleted successfully!');
        },
        error => console.error('Error:', error)
      );
  }

  startRecording() {
    this.isRecording = true;
    navigator.mediaDevices.getUserMedia({ audio: true })
      .then(stream => {
        this.mediaRecorder = new MediaRecorder(stream);
        this.mediaRecorder.start();

        this.mediaRecorder.addEventListener("dataavailable", event => {
          this.audioChunks.push(event.data);
        });

        this.mediaRecorder.addEventListener("stop", () => {
          const audioBlob = new Blob(this.audioChunks);
          this.sendAudioToServer(audioBlob);
        });
      });
  }

  stopRecording() {
    this.isRecording = false;
    if (this.mediaRecorder) {
      this.mediaRecorder.stop();
    }
  }

  sendAudioToServer(audioBlob: Blob) {
    const formData = new FormData();
    formData.append('file', audioBlob, 'recording.wav');

    this.http.post('http://localhost:5000/api/speech-to-text', formData)
      .subscribe(
        (response: any) => {
          if (response.success) {
            this.text = response.text;
          }
        },
        error => console.error('Error:', error)
      );
  }
}
