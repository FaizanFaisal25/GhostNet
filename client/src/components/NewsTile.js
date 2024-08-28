import React from "react";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faCommentDots } from "@fortawesome/free-solid-svg-icons";
import { useNavigate } from "react-router-dom";
import { profilePicturesDir } from "../config";
import { getProfilePicturePath } from "../util";

const NewsTile = ({ article, onClickTrue }) => {
  const navigate = useNavigate();

  const handlePostClick = () => {
    navigate(`/post/${article.id}`);
  };

  return (
    <div
      className={`border rounded-lg shadow-lg overflow-hidden ${
        onClickTrue
          ? "hover:bg-blue-100 transform ransition-transform duration-300"
          : ""
      }`}
      onClick={onClickTrue ? handlePostClick : () => {}}
    >
      <img
        src={article.url_to_image || "https://via.placeholder.com/300"}
        alt={article.title}
        className="w-full h-48 object-cover"
      />
      <div className="p-4">
        <div className="flex items-center space-x-4">
          <img
            src={getProfilePicturePath(article.author_profile_photo)}
            alt="Profile Photo"
            className="w-10 h-10 rounded-full object-cover"
          />
          <div className="text-lg font-medium">{article.author_name}</div>
        </div>
        <h2 className="text-xl font-semibold mb-2">{article.title}</h2>
        <p className="text-gray-700 mb-4">{article.description}</p>
        <a
          href={article.url}
          target="_blank"
          rel="noopener noreferrer"
          className="text-blue-500 hover:underline"
        >
          Read more
        </a>
        <div className="flex items-center mt-4">
          <button
            className="flex items-center text-gray-700 hover:text-gray-900"
            onClick={onClickTrue ? handlePostClick : () => {}}
          >
            <FontAwesomeIcon icon={faCommentDots} className="mr-2" />
            Comments
          </button>
        </div>
      </div>
    </div>
  );
};

export default NewsTile;
