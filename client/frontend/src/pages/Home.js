import React, { useEffect, useState } from 'react';
import NewsTile from '../components/NewsTile';

const Home = () => {
    const [news, setNews] = useState([]);

    useEffect(() => {
        const fetchNews = async () => {
            try {
                const response = await fetch('http://localhost:9988/get_news');
                const data = await response.json();
                if (data.status === 'ok') {
                    setNews(data.articles);
                }
            } catch (error) {
                console.error('Error fetching news:', error);
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
                        <NewsTile article={article} />
                    </div>
                ))}
            </div>
        </div>
    );
};

export default Home;
