import React from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faCommentDots } from '@fortawesome/free-solid-svg-icons';
import { useNavigate } from 'react-router-dom';

const NewsTile = ({ article }) => {
    const navigate = useNavigate();

    const handleCommentsClick = () => {
        navigate('/post');
    };

    return (
        <div className="border rounded-lg shadow-lg overflow-hidden">
            <img
                src={article.urlToImage || 'https://via.placeholder.com/300'}
                alt={article.title}
                className="w-full h-48 object-cover"
            />
            <div className="p-4">
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
                        onClick={handleCommentsClick}
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
