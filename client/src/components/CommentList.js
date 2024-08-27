import React from "react";
import Comment from "./Comment";
import { formatHumanReadableDate } from "../util";

const CommentList = ({ comments }) => {
  return (
    <div>
      {comments.map((comment, index) => (
        <div className="my-2" key={index}>
          <Comment
            authorName={comment.author_name}
            authorPicture={comment.author_profile_photo}
            content={comment.content}
            date={formatHumanReadableDate(comment.published_at)}
          />
        </div>
      ))}
    </div>
  );
};
export default CommentList;
