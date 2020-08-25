CREATE TABLE youtube_data(
    id SERIAL PRIMARY KEY,
    video_tag VARCHAR NOT NULL,
    video_title VARCHAR NOT NULL,
    video_description VARCHAR NOT NULL,
    channel_tag VARCHAR NOT NULL,
    channel_title VARCHAR NOT NULL,
    publish_time VARCHAR NOT NULL,
    thumbnail VARCHAR NOT NULL
);