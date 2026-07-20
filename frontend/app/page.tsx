export default function Home() {
  return (
    <main className="min-h-screen flex flex-col items-center justify-center gap-6">
      <h1 className="text-5xl font-bold">
        🎤 VocalSplit
      </h1>

      <p>Upload a song to generate karaoke.</p>

      <input type="file" accept=".mp3,audio/*" />

      <button className="bg-black text-white px-6 py-3 rounded-xl">
        Upload
      </button>
    </main>
  );
}