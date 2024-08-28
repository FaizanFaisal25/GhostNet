import React from "react";
import { getProfilePicturePath } from "../util";

const Comment = ({ authorName, authorPicture, content, date }) => {
  return (
    <div className="bg-white border shadow-md rounded-lg p-4 mx-auto my-4">
      <div className="flex items-center mb-4">
        {/* <img
          className="w-12 h-12 rounded-full mr-4"
          src={getProfilePicturePath(authorPicture)}
          alt={`${authorName}'s profile`}
        /> */}
        <div>
          <h2 className="text-lg font-semibold">{authorName}</h2>
          {/* <p className="text-gray-500 text-sm">{date}</p> */}
        </div>
      </div>
      <p className="text-gray-700">{content}</p>
    </div>
  );
};
export default Comment;
