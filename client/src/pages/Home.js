import React, { useEffect, useState } from "react";
import NewsTile from "../components/NewsTile";
import { createURL } from "../config";

const Home = () => {
  const [news, setNews] = useState([]);

  useEffect(() => {
    const fetchNews = async () => {
      try {
        const response = await fetch(createURL("get_all_posts"));
        if (response.ok) {
          const data = await response.json();
          setNews(data);

          console.log(data);
        } else {
          throw new Error(`Error: ${response.status}`);
        }
      } catch (error) {
        console.error("Error fetching news:", error);
      }
    };

    fetchNews();
  }, []);

  return (
    <div className="flex flex-col items-center p-4">
      <h1 className="text-3xl font-bold mb-6">News Feed</h1>
      <div className="w-full max-w-4xl">
        {news.map((article, index) => (
          <div className="mb-4" key={index}>
            <NewsTile article={article} onClickTrue={true} />
          </div>
        ))}
      </div>
    </div>
  );
};

export default Home;
