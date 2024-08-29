import React from "react";
import Comment from "./Comment";
import { formatHumanReadableDate } from "../util";

const CommentList = ({ comments }) => {
  return (
    <div>
      {comments.map((comment, index) => (
        <div className="my-2" key={index}>
          <Comment
            authorName={comment[0].name}
            authorPicture={comment[0].id}
            content={comment[1]}
            date={formatHumanReadableDate(comment.published_at)}
          />
        </div>
      ))}
    </div>
  );
};
export default CommentList;
