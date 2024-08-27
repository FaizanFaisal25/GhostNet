import React, { useState, useEffect } from "react";
import { useParams } from "react-router-dom";
import NewsTile from "../components/NewsTile";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faArrowRight } from "@fortawesome/free-solid-svg-icons";

const Post = () => {
  const { postId } = useParams();
  const [article, setArticle] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // Replace the URL with your API endpoint
    const fetchArticle = async () => {
      try {
        const response = await fetch(`/api/articles/${1}`);
        if (!response.ok) {
          throw new Error("Failed to fetch article data");
        }
        const data = await response.json();
        setArticle(data);
      } catch (error) {
        console.error("Error fetching article:", error);
      } finally {
        setLoading(false);
      }
    };

    fetchArticle();
  }, [postId]);

  if (loading) {
    return <p>Loading...</p>;
  }

  return (
    <div className="container mx-auto p-4">
      {article ? (
        <div>
          <NewsTile article={article} onClickTrue={false} />
          <div className="mt-8">
            <h3 className="text-2xl font-semibold mb-4">Comments on {postId}</h3>
            <div className="typing">
              <div className="typing__dot"></div>
              <div className="typing__dot"></div>
              <div className="typing__dot"></div>
            </div>
            <textarea
              className="w-full p-2 border rounded-md"
              placeholder="Add a comment..."
            ></textarea>
            <button className="mt-2 px-4 py-2 bg-black text-white rounded-md hover:bg-blue-800 flex items-center">
              Post Comment
              <FontAwesomeIcon icon={faArrowRight} className="ml-2" />
            </button>
          </div>
        </div>
      ) : (
        <p>No article data found.</p>
      )}
    </div>
  );
};

export default Post;

