import { APIEndpoint, profilePicturesDir } from "./config";

export const createURL = (url) => {
  return `${APIEndpoint}${url}`;
};

export const formatHumanReadableDate = (isoString) => {
  // Create a new Date object from the ISO string
  const date = new Date(isoString);

  // Define options for formatting the date and time, without the time zone
  const options = {
    year: "numeric",
    month: "long",
    day: "numeric",
    hour: "2-digit",
    minute: "2-digit",
    second: "2-digit",
    hour12: true, // Optional: to display time in 12-hour format with AM/PM
  };

  // Format the date using toLocaleDateString with the given options
  const humanReadableDate = date.toLocaleString("en-US", options);

  return humanReadableDate;
};

export const getProfilePicturePath = (imagePath) => {
  return `/${profilePicturesDir}/${imagePath}`;
};
