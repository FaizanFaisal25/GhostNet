import React from "react";
import { useLocation } from "react-router-dom";
import NewsTile from "../components/NewsTile";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faArrowRight } from "@fortawesome/free-solid-svg-icons";

const Post = () => {
  const location = useLocation();
  const article = location.state?.article;

  return (
    <div className="container mx-auto p-4">
      {article ? (
        <div>
          <NewsTile article={article} onClickTrue={false} />
          <div className="mt-8">
            <h3 className="text-2xl font-semibold mb-4">Comments</h3>
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
