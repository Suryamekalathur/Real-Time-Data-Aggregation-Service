
import React, { useEffect, useState } from "react";

function App() {

  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch("http://localhost:8000/rates")
      .then(res => res.json())
      .then(data => {
        setData(data);
        setLoading(false);
      });
  }, []);

  if (loading) return <h2>Loading...</h2>;

  if (data.error) return <h2>Error fetching data</h2>;

  const timestamp = new Date(data.timestamp);
  const now = new Date();

  const diff = Math.floor((now - timestamp) / 60000);

  let freshness = "Fresh";
  if (diff > 30) freshness = "Stale";
  else if (diff > 5) freshness = "Slightly Stale";

  return (
    <div style={{ padding: "20px" }}>
      <h1>Forex Rate Tracker</h1>

      <h3>USD → INR: {data.rates.INR}</h3>
      <h3>USD → EUR: {data.rates.EUR}</h3>
      <h3>USD → GBP: {data.rates.GBP}</h3>

      <p>Source: {data.source}</p>
      <p>Freshness: {freshness}</p>
      <p>Last Updated: {timestamp.toLocaleString()}</p>

      {data.cached && (
        <p style={{color:"red"}}>Using cached data</p>
      )}

    </div>
  );
}

export default App;
