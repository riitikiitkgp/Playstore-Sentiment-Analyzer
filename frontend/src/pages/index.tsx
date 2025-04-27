import { useState } from "react";

export default function Home() {
  const [appName, setAppName] = useState<string>("");
  const [loading, setLoading] = useState<boolean>(false);
  const [result, setResult] = useState<any>(null);

  const handleAnalyze = async () => {
    setLoading(true);
    const res = await fetch("http://localhost:8000/analyze", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ appName }),
    });

    const data = await res.json();
    setResult(data);
    setLoading(false);
  };

  return (
    <div>
      <h1>Playstore Sentiment Analyzer</h1>
      <input
        type="text"
        placeholder="Enter App Name"
        value={appName}
        onChange={(e) => setAppName(e.target.value)}
        autoComplete="off"
      />
      <button onClick={handleAnalyze} disabled={loading}>
        {loading ? "Analyzing..." : "Analyze"}
      </button>

      {result && (
        <div>
          <h2>Results:</h2>
          <p>Average Sentiment Score: {result.average_sentiment_score}</p>
          <p>Number of Reviews Analyzed: {result.number_of_reviews}</p>
        </div>
      )}
    </div>
  );
}
