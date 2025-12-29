CREATE DATABASE IF NOT EXISTS social_media_db;
USE social_media_db;

-- Users Table
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE,
    email VARCHAR(100) UNIQUE,
    password_hash VARCHAR(255),
    timezone VARCHAR(50) DEFAULT 'UTC',
    target_audience_json JSON
);

-- Platforms Table
CREATE TABLE IF NOT EXISTS platforms (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    platform_name VARCHAR(50),
    platform_username VARCHAR(50),
    preferences_json JSON,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

-- Content Drafts Table
CREATE TABLE IF NOT EXISTS content_drafts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    original_text TEXT,
    media_path VARCHAR(255),
    target_platforms JSON,
    status VARCHAR(20) DEFAULT 'draft',
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

-- Optimized Content Table
CREATE TABLE IF NOT EXISTS optimized_content (
    id INT AUTO_INCREMENT PRIMARY KEY,
    draft_id INT,
    platform_id INT,
    platform_name VARCHAR(50),
    optimized_text TEXT,
    hashtags JSON,
    recommendations_json JSON,
    score INT,
    FOREIGN KEY (draft_id) REFERENCES content_drafts(id)
);

-- Posting Schedule Table
CREATE TABLE IF NOT EXISTS posting_schedule (
    id INT AUTO_INCREMENT PRIMARY KEY,
    draft_id INT,
    platform_id INT,
    platform_name VARCHAR(50),
    scheduled_datetime DATETIME,
    posted INT DEFAULT 0,
    performance_notes TEXT,
    FOREIGN KEY (draft_id) REFERENCES content_drafts(id)
);

-- Research Cache Table
CREATE TABLE IF NOT EXISTS research_cache (
    id INT AUTO_INCREMENT PRIMARY KEY,
    platform_name VARCHAR(50),
    research_topic VARCHAR(100),
    findings_json JSON,
    researched_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Posting Analytics Table
CREATE TABLE IF NOT EXISTS posting_analytics (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    platform_name VARCHAR(50),
    best_times_json JSON,
    audience_insights_json JSON,
    last_updated DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id)
);
