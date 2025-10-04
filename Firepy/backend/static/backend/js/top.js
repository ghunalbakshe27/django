// Song data
const songs = [
  {
        id: 1,
        title: "Chaleya",
        artist: "Arijit Singh",
        src: "/media/songs/Chaleya.mp3",
        img: "/media/images/Chaleya.jpg"
      },
      {
        id: 2,
        title: "Aasa Kooda",
        artist: "Sai Abhyankkar, Sai Smriti",
        src: "/media/songs/Aasa Kooda.mp3",
        img: "/media/images/Aasa_Kooda.jpeg"
      },
      {
        id: 3,
        title: "Hukum",
        artist: "Anirudh Ravichander",
        src: "/media/songs/Hukum.mp3",
        img: "/media/images/Hukum.webp"
      },
      {
        id: 4,
        title: "Heat Waves",
        artist: "Glass Animals",
        src: "/media/songs/Heat_Waves_Glass_Animals.mp3",
        img: "/media/images/Heat_Waves_Glass_Animals.jpeg"
      },
      {
        id: 5,
        title: "Sweater Weather",
        artist: "The Neighbourhood",
        src: "/media/songs/Sweater Weather.mp3",
        img: "/media/images/Sweater Weather.jpeg"
      },
      {
        id: 6,
        title: "Ghungroo",
        artist: "Arijit Singh",
        src: "/media/songs/Ghungroo.mp3",
        img: "/media/images/Ghungroo.jpeg"
      },
      {
        id: 7,
        title: "Pehle Bhi Main",
        artist: "Vishal Mishra",
        src: "/media/songs/PEHLE BHI MAIN.mp3",
        img: "/media/images/PEHLE BHI MAIN.jpeg"
      },
      {
        id: 8,
        title: "Satranga",
        artist: "Arijit Singh",
        src: "/media/songs/Satranga.mp3",
        img: "/media/images/Satranga.jpg"
      },
      {
        id: 9,
        title: "Akhiyaan Gulaab",
        artist: "Mitraz",
        src: "/media/songs/Akhiyaan Gulaab.mp3",
        img: "/media/images/Akhiyaan Gulaab.jpeg"
      },
      {
        id: 10,
        title: "Tum Kya Mile",
        artist: "Arijit Singh, Shreya Ghoshal",
        src: "/media/songs/Tum Kya Mile.mp3",
        img: "/media/images/Tum Kya Mile.jpeg"
      },
      {
        id: 11,
        title: "Tauba Tauba",
        artist: "Karan Aujla",
        src: "/media/songs/Tauba Tauba.mp3",
        img: "/media/images/Tauba Tauba.jpeg"
      }
];

// Global variables
let currentIndex = 0;
let isPlaying = false;

// DOM elements
const songsList = document.getElementById("songsList");
const bottomPlayer = document.getElementById("bottomPlayer");
const playPauseBtn = document.getElementById("playPauseBtn");
const bottomSongTitle = document.getElementById("bottomSongTitle");
const bottomSongArtist = document.getElementById("bottomSongArtist");
const bottomSongImg = document.getElementById("bottomSongImg");
const audio = document.getElementById("audioPlayer");
const fullPlayer = document.getElementById("fullPlayer");
const closeFull = document.getElementById("closeFull");
const fullSongImg = document.getElementById("fullSongImg");
const fullSongTitle = document.getElementById("fullSongTitle");
const fullSongArtist = document.getElementById("fullSongArtist");
const fullPlayPauseBtn = document.getElementById("fullPlayPauseBtn");

// Functions
function renderSongs() {
  songsList.innerHTML = songs.map((song, index) => `
    <div class="song-item ${index === currentIndex ? 'active' : ''}" data-id="${song.id}" style="animation-delay: ${index * 0.1}s">
      <img src="${song.img}" class="song-thumb" alt="${song.title}">
      <div class="song-info">
        <div class="song-title">${song.title}</div>
        <div class="song-artist">${song.artist}</div>
      </div>
    </div>
  `).join("");
}

function playSong(index) {
  currentIndex = index;
  const song = songs[currentIndex];
  audio.src = song.src;
  audio.play().catch(e => {
    console.log('Playback failed:', e);
    isPlaying = false;
    updateUI();
  });
  isPlaying = true;

  // Update bottom player (no arrow)
  bottomSongTitle.textContent = song.title;
  bottomSongArtist.textContent = song.artist;
  bottomSongImg.src = song.img;
  bottomPlayer.classList.add("show");

  // Update full player (with arrow)
  fullSongTitle.innerHTML = `<span style="color: gray; margin-right: 8px;font-size:52px;">⇛</span>${song.title}`;
  fullSongArtist.textContent = song.artist;
  fullSongImg.src = song.img;

  updateUI();
  renderSongs();
}

function togglePlay() {
  if (isPlaying) {
    audio.pause();
    isPlaying = false;
  } else {
    audio.play().catch(e => {
      console.log('Playback failed:', e);
      isPlaying = false;
    });
    isPlaying = !audio.paused;
  }
  updateUI();
  renderSongs();
}

function playNext() {
  currentIndex = (currentIndex + 1) % songs.length;
  playSong(currentIndex);
}

function playPrev() {
  currentIndex = (currentIndex - 1 + songs.length) % songs.length;
  playSong(currentIndex);
}

function updateUI() {
  playPauseBtn.textContent = isPlaying ? "◼" : "▶";
  fullPlayPauseBtn.textContent = isPlaying ? "◼" : "▶";
}

function showFullPlayer() {
  fullPlayer.classList.add("show");
  document.body.style.overflow = 'hidden';
}

function hideFullPlayer() {
  fullPlayer.classList.remove("show");
  document.body.style.overflow = 'auto';
}

// Event listeners
audio.addEventListener("ended", playNext);

audio.addEventListener("play", () => {
  isPlaying = true;
  updateUI();
  renderSongs();
});

audio.addEventListener("pause", () => {
  isPlaying = false;
  updateUI();
  renderSongs();
});

audio.addEventListener("error", (e) => {
  console.log('Audio error:', e);
  isPlaying = false;
  updateUI();
});

// Song list events
songsList.addEventListener("click", (e) => {
  const item = e.target.closest(".song-item");
  if (!item) return;
  const id = parseInt(item.dataset.id);
  const index = songs.findIndex(s => s.id === id);
  if (index !== -1) {
    if (index === currentIndex && isPlaying) {
      togglePlay();
    } else {
      playSong(index);
    }
  }
});

// Bottom player events
playPauseBtn.addEventListener("click", (e) => {
  e.stopPropagation();
  togglePlay();
});

document.getElementById("nextBtn").addEventListener("click", (e) => {
  e.stopPropagation();
  playNext();
});

document.getElementById("prevBtn").addEventListener("click", (e) => {
  e.stopPropagation();
  playPrev();
});

bottomPlayer.addEventListener("click", showFullPlayer);

// Full player events
fullPlayPauseBtn.addEventListener("click", togglePlay);
document.getElementById("fullNextBtn").addEventListener("click", playNext);
document.getElementById("fullPrevBtn").addEventListener("click", playPrev);
closeFull.addEventListener("click", hideFullPlayer);

// Keyboard shortcuts
document.addEventListener("keydown", (e) => {
  if (e.code === 'Space' && !e.target.matches('input, textarea')) {
    e.preventDefault();
    togglePlay();
  } else if (e.code === 'ArrowRight') {
    playNext();
  } else if (e.code === 'ArrowLeft') {
    playPrev();
  } else if (e.code === 'Escape' && fullPlayer.classList.contains('show')) {
    hideFullPlayer();
  }
});

// Handle visibility change (when user switches tabs)
document.addEventListener("visibilitychange", () => {
  if (document.hidden && isPlaying) {
    // Keep playing when tab is hidden
  }
});

// Initialize
renderSongs();

// Auto-play first song on user interaction (required by browsers)
document.addEventListener("click", function initAudioContext() {
  if (audio.readyState >= 2 && !audio.src) {
    // Audio context is ready, we can now play audio
  }
}, { once: true });




// // Song data
// // Song data
// // Song data
// const songs = [
//   {
//         id: 1,
//         title: "Chaleya",
//         artist: "Arijit Singh",
//         src: "/media/songs/Chaleya.mp3",
//         img: "/media/images/Chaleya.jpg"
//       },
//       {
//         id: 2,
//         title: "Aasa Kooda",
//         artist: "Sai Abhyankkar, Sai Smriti",
//         src: "/media/songs/Aasa Kooda.mp3",
//         img: "/media/images/Aasa_Kooda.jpeg"
//       },
//       {
//         id: 3,
//         title: "Hukum",
//         artist: "Anirudh Ravichander",
//         src: "/media/songs/Hukum.mp3",
//         img: "/media/images/Hukum.webp"
//       },
//       {
//         id: 4,
//         title: "Heat Waves",
//         artist: "Glass Animals",
//         src: "/media/songs/Heat Waves (Glass Animals ).mp3",
//         img: "/media/images/Heat_Waves_Glass_Animals.jpeg"
//       },
//       {
//         id: 5,
//         title: "Sweater Weather",
//         artist: "The Neighbourhood",
//         src: "/media/songs/Sweater Weather.mp3",
//         img: "/media/images/Sweater Weather.jpeg"
//       },
//       {
//         id: 6,
//         title: "Ghungroo",
//         artist: "Arijit Singh",
//         src: "/media/songs/Ghungroo.mp3",
//         img: "/media/images/Ghungroo.jpeg"
//       },
//       {
//         id: 7,
//         title: "Pehle Bhi Main",
//         artist: "Vishal Mishra",
//         src: "/media/songs/PEHLE BHI MAIN.mp3",
//         img: "/media/images/PEHLE BHI MAIN.jpeg"
//       },
//       {
//         id: 8,
//         title: "Satranga",
//         artist: "Arijit Singh",
//         src: "/media/songs/Satranga.mp3",
//         img: "/media/images/Satranga.jpg"
//       },
//       {
//         id: 9,
//         title: "Akhiyaan Gulaab",
//         artist: "Mitraz",
//         src: "/media/songs/Akhiyaan Gulaab.mp3",
//         img: "/media/images/Akhiyaan Gulaab.jpeg"
//       },
//       {
//         id: 10,
//         title: "Tum Kya Mile",
//         artist: "Arijit Singh, Shreya Ghoshal",
//         src: "/media/songs/Tum Kya Mile.mp3",
//         img: "/media/images/Tum Kya Mile.jpeg"
//       },
//       {
//         id: 11,
//         title: "Tauba Tauba",
//         artist: "Karan Aujla",
//         src: "/media/songs/Tauba Tauba.mp3",
//         img: "/media/images/Tauba Tauba.jpeg"
//       }
// ];

// // Global variables
// let currentIndex = 0;
// let isPlaying = false;

// // DOM elements
// const songsList = document.getElementById("songsList");
// const bottomPlayer = document.getElementById("bottomPlayer");
// const playPauseBtn = document.getElementById("playPauseBtn");
// const bottomSongTitle = document.getElementById("bottomSongTitle");
// const bottomSongArtist = document.getElementById("bottomSongArtist");
// const bottomSongImg = document.getElementById("bottomSongImg");
// const audio = document.getElementById("audioPlayer");
// const fullPlayer = document.getElementById("fullPlayer");
// const closeFull = document.getElementById("closeFull");
// const fullSongImg = document.getElementById("fullSongImg");
// const fullSongTitle = document.getElementById("fullSongTitle");
// const fullSongArtist = document.getElementById("fullSongArtist");
// const fullPlayPauseBtn = document.getElementById("fullPlayPauseBtn");
// const fullProgressBar = document.getElementById("fullProgressBar");
// const currentTimeEl = document.getElementById("currentTime");
// const totalTimeEl = document.getElementById("totalTime");
// const progressContainer = document.getElementById("progressContainer");
// const progressBarBg = document.getElementById("progressBarBg");
// const progressHandle = document.getElementById("progressHandle");

// // Drag functionality variables
// let isDragging = false;
// let wasPlaying = false;

// // Functions
// function renderSongs() {
//   songsList.innerHTML = songs.map((song, index) => `
//     <div class="song-item ${index === currentIndex ? 'active' : ''}" data-id="${song.id}" style="animation-delay: ${index * 0.1}s">
//       <img src="${song.img}" class="song-thumb" alt="${song.title}">
//       <div class="song-info">
//         <div class="song-title">${song.title}</div>
//         <div class="song-artist">${song.artist}</div>
//       </div>
//     </div>
//   `).join("");
// }

// function playSong(index) {
//   currentIndex = index;
//   const song = songs[currentIndex];
//   audio.src = song.src;
//   audio.play().catch(e => {
//     console.log('Playback failed:', e);
//     isPlaying = false;
//     updateUI();
//   });
//   isPlaying = true;

//   // Show progress handle when song is loaded
//   progressHandle.classList.add("visible");

//   // Update bottom player (no arrow)
//   bottomSongTitle.textContent = song.title;
//   bottomSongArtist.textContent = song.artist;
//   bottomSongImg.src = song.img;
//   bottomPlayer.classList.add("show");

//   // Update full player (with arrow)
//   fullSongTitle.innerHTML = `<span style="color: gray; margin-right: 8px;font-size:52px;">⇛</span>${song.title}`;
//   fullSongArtist.textContent = song.artist;
//   fullSongImg.src = song.img;

//   updateUI();
//   renderSongs();
// }

// function togglePlay() {
//   if (isPlaying) {
//     audio.pause();
//     isPlaying = false;
//   } else {
//     audio.play().catch(e => {
//       console.log('Playback failed:', e);
//       isPlaying = false;
//     });
//     isPlaying = !audio.paused;
//   }
//   // Keep handle visible regardless of play/pause state
//   if (audio.src) {
//     progressHandle.classList.add("visible");
//   }
//   updateUI();
//   renderSongs();
// }

// function playNext() {
//   currentIndex = (currentIndex + 1) % songs.length;
//   playSong(currentIndex);
// }

// function playPrev() {
//   currentIndex = (currentIndex - 1 + songs.length) % songs.length;
//   playSong(currentIndex);
// }

// function updateUI() {
//   playPauseBtn.textContent = isPlaying ? "◼" : "▶";
//   fullPlayPauseBtn.textContent = isPlaying ? "◼" : "▶";
// }

// function formatTime(seconds) {
//   const mins = Math.floor(seconds / 60);
//   const secs = Math.floor(seconds % 60);
//   return `${mins}:${secs.toString().padStart(2, '0')}`;
// }

// function showFullPlayer() {
//   fullPlayer.classList.add("show");
//   document.body.style.overflow = 'hidden';
// }

// function hideFullPlayer() {
//   fullPlayer.classList.remove("show");
//   document.body.style.overflow = 'auto';
// }

// // Enhanced progress bar with drag functionality
// function updateProgressFromPosition(clientX) {
//   const rect = progressBarBg.getBoundingClientRect();
//   const clickX = clientX - rect.left;
//   const width = rect.width;
//   const percentage = Math.max(0, Math.min(1, clickX / width));
  
//   if (audio.duration) {
//     const newTime = percentage * audio.duration;
//     if (!isDragging) {
//       audio.currentTime = newTime;
//     }
    
//     fullProgressBar.style.width = (percentage * 100) + "%";
//     currentTimeEl.textContent = formatTime(newTime);
    
//     return newTime;
//   }
//   return 0;
// }

// // Event listeners
// audio.addEventListener("timeupdate", () => {
//   if (audio.duration && !isDragging) {
//     const progress = (audio.currentTime / audio.duration) * 100;
//     fullProgressBar.style.width = progress + "%";
//     currentTimeEl.textContent = formatTime(audio.currentTime);
//   }
// });

// audio.addEventListener("loadedmetadata", () => {
//   if (audio.duration) {
//     totalTimeEl.textContent = formatTime(audio.duration);
//   }
// });

// audio.addEventListener("ended", playNext);

// audio.addEventListener("play", () => {
//   isPlaying = true;
//   updateUI();
//   renderSongs();
// });

// audio.addEventListener("pause", () => {
//   isPlaying = false;
//   updateUI();
//   renderSongs();
// });

// audio.addEventListener("error", (e) => {
//   console.log('Audio error:', e);
//   isPlaying = false;
//   updateUI();
// });

// // Click on progress bar
// progressBarBg.addEventListener("click", (e) => {
//   if (!isDragging) {
//     const newTime = updateProgressFromPosition(e.clientX);
//     if (audio.duration) {
//       audio.currentTime = newTime;
//     }
//   }
// });

// // Mouse drag events for progress handle
// progressHandle.addEventListener("mousedown", (e) => {
//   e.preventDefault();
//   isDragging = true;
//   wasPlaying = isPlaying;
//   progressHandle.classList.add("dragging");
  
//   if (wasPlaying) {
//     audio.pause();
//   }
// });

// document.addEventListener("mousemove", (e) => {
//   if (isDragging) {
//     updateProgressFromPosition(e.clientX);
//   }
// });

// document.addEventListener("mouseup", (e) => {
//   if (isDragging) {
//     isDragging = false;
//     progressHandle.classList.remove("dragging");
    
//     const newTime = updateProgressFromPosition(e.clientX);
//     if (audio.duration) {
//       audio.currentTime = newTime;
//     }
    
//     if (wasPlaying) {
//       audio.play();
//     }
//   }
// });

// // Touch events for mobile support
// progressHandle.addEventListener("touchstart", (e) => {
//   e.preventDefault();
//   isDragging = true;
//   wasPlaying = isPlaying;
//   progressHandle.classList.add("dragging");
  
//   if (wasPlaying) {
//     audio.pause();
//   }
// }, { passive: false });

// document.addEventListener("touchmove", (e) => {
//   if (isDragging && e.touches[0]) {
//     e.preventDefault();
//     updateProgressFromPosition(e.touches[0].clientX);
//   }
// }, { passive: false });

// document.addEventListener("touchend", (e) => {
//   if (isDragging) {
//     isDragging = false;
//     progressHandle.classList.remove("dragging");
    
//     const touch = e.changedTouches[0];
//     if (touch) {
//       const newTime = updateProgressFromPosition(touch.clientX);
//       if (audio.duration) {
//         audio.currentTime = newTime;
//       }
//     }
    
//     if (wasPlaying) {
//       audio.play();
//     }
//   }
// });

// // Song list events
// songsList.addEventListener("click", (e) => {
//   const item = e.target.closest(".song-item");
//   if (!item) return;
//   const id = parseInt(item.dataset.id);
//   const index = songs.findIndex(s => s.id === id);
//   if (index !== -1) {
//     if (index === currentIndex && isPlaying) {
//       togglePlay();
//     } else {
//       playSong(index);
//     }
//   }
// });

// // Bottom player events
// playPauseBtn.addEventListener("click", (e) => {
//   e.stopPropagation();
//   togglePlay();
// });

// document.getElementById("nextBtn").addEventListener("click", (e) => {
//   e.stopPropagation();
//   playNext();
// });

// document.getElementById("prevBtn").addEventListener("click", (e) => {
//   e.stopPropagation();
//   playPrev();
// });

// bottomPlayer.addEventListener("click", showFullPlayer);

// // Full player events
// fullPlayPauseBtn.addEventListener("click", togglePlay);
// document.getElementById("fullNextBtn").addEventListener("click", playNext);
// document.getElementById("fullPrevBtn").addEventListener("click", playPrev);
// closeFull.addEventListener("click", hideFullPlayer);

// // 5s Forward/Backward controls
// document.getElementById("backward5Btn").addEventListener("click", () => {
//   audio.currentTime = Math.max(0, audio.currentTime - 5);
// });

// document.getElementById("forward5Btn").addEventListener("click", () => {
//   if (audio.duration) {
//     audio.currentTime = Math.min(audio.duration, audio.currentTime + 5);
//   }
// });

// // Keyboard shortcuts
// document.addEventListener("keydown", (e) => {
//   if (e.code === 'Space' && !e.target.matches('input, textarea')) {
//     e.preventDefault();
//     togglePlay();
//   } else if (e.code === 'ArrowRight') {
//     playNext();
//   } else if (e.code === 'ArrowLeft') {
//     playPrev();
//   } else if (e.code === 'Escape' && fullPlayer.classList.contains('show')) {
//     hideFullPlayer();
//   }
// });

// // Handle visibility change (when user switches tabs)
// document.addEventListener("visibilitychange", () => {
//   if (document.hidden && isPlaying) {
//     // Keep playing when tab is hidden
//   }
// });

// // Prevent context menu on long press (mobile)
// document.addEventListener("contextmenu", (e) => {
//   if (e.target.closest(".progress-handle") || e.target.closest(".progress-bar-bg")) {
//     e.preventDefault();
//   }
// });

// // Initialize
// renderSongs();

// // Auto-play first song on user interaction (required by browsers)
// document.addEventListener("click", function initAudioContext() {
//   if (audio.readyState >= 2 && !audio.src) {
//     // Audio context is ready, we can now play audio
//   }
// }, { once: true });