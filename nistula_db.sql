
-- NISTULA UNIFIED MESSAGING PLATFORM SCHEMA
-- MySQL Compatible Version

-- CREATE DATABASE

CREATE DATABASE IF NOT EXISTS nistula_db;

USE nistula_db;
-- GUESTS
-- One unified guest record across all channels

CREATE TABLE guests (
    guest_id CHAR(36) PRIMARY KEY,

    first_name VARCHAR(100),
    last_name VARCHAR(100),

    email VARCHAR(255) UNIQUE,
    phone VARCHAR(30),

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- =====================================================
-- GUEST CHANNEL PROFILES
-- Stores external platform IDs for each guest
-- Example:
-- WhatsApp number
-- Airbnb guest ID
-- Booking.com guest ID
-- =====================================================

CREATE TABLE guest_channel_profiles (
    profile_id CHAR(36) PRIMARY KEY,

    guest_id CHAR(36) NOT NULL,

    channel ENUM(
        'whatsapp',
        'email',
        'sms',
        'airbnb',
        'booking_com',
        'webchat',
        'phone'
    ) NOT NULL,

    external_user_id VARCHAR(255) NOT NULL,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    UNIQUE(channel, external_user_id),

    FOREIGN KEY (guest_id)
        REFERENCES guests(guest_id)
        ON DELETE CASCADE
);
-- RESERVATIONS
-- Reservation linked to guest

CREATE TABLE reservations (
    reservation_id CHAR(36) PRIMARY KEY,

    guest_id CHAR(36) NOT NULL,

    property_id CHAR(36),

    external_reservation_id VARCHAR(255),

    check_in_date DATE,
    check_out_date DATE,

    reservation_status VARCHAR(50),

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (guest_id)
        REFERENCES guests(guest_id)
        ON DELETE CASCADE
);


-- CONVERSATIONS
-- Conversation thread linked to guest + reservation

CREATE TABLE conversations (
    conversation_id CHAR(36) PRIMARY KEY,

    guest_id CHAR(36) NOT NULL,

    reservation_id CHAR(36),

    channel ENUM(
        'whatsapp',
        'email',
        'sms',
        'airbnb',
        'booking_com',
        'webchat',
        'phone'
    ) NOT NULL,

    subject VARCHAR(255),

    is_active BOOLEAN DEFAULT TRUE,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (guest_id)
        REFERENCES guests(guest_id)
        ON DELETE CASCADE,

    FOREIGN KEY (reservation_id)
        REFERENCES reservations(reservation_id)
        ON DELETE SET NULL
);

-- MESSAGES
-- Unified table storing all inbound and outbound messages


CREATE TABLE messages (
    message_id CHAR(36) PRIMARY KEY,

    conversation_id CHAR(36) NOT NULL,

    external_message_id VARCHAR(255),

    direction ENUM(
        'inbound',
        'outbound'
    ) NOT NULL,

    sender ENUM(
        'guest',
        'ai',
        'agent',
        'system'
    ) NOT NULL,

    message_body TEXT NOT NULL,

    channel ENUM(
        'whatsapp',
        'email',
        'sms',
        'airbnb',
        'booking_com',
        'webchat',
        'phone'
    ) NOT NULL,

    message_status ENUM(
        'draft',
        'queued',
        'sent',
        'delivered',
        'read',
        'failed'
    ) DEFAULT 'sent',

    -- AI workflow tracking
    ai_drafted BOOLEAN DEFAULT FALSE,
    agent_edited BOOLEAN DEFAULT FALSE,
    auto_sent BOOLEAN DEFAULT FALSE,

    -- AI metadata for inbound messages
    ai_confidence_score DECIMAL(5,4),

    ai_query_type ENUM(
        'booking_inquiry',
        'reservation_change',
        'payment_issue',
        'check_in',
        'check_out',
        'cancellation',
        'complaint',
        'faq',
        'other'
    ),

    sent_at TIMESTAMP NULL,
    delivered_at TIMESTAMP NULL,
    read_at TIMESTAMP NULL,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (conversation_id)
        REFERENCES conversations(conversation_id)
        ON DELETE CASCADE
);


-- INDEXES
-- Improves query performance

CREATE INDEX idx_messages_conversation
ON messages(conversation_id);

CREATE INDEX idx_messages_channel
ON messages(channel);

CREATE INDEX idx_messages_created_at
ON messages(created_at);

CREATE INDEX idx_conversations_guest
ON conversations(guest_id);

CREATE INDEX idx_reservations_guest
ON reservations(guest_id);


