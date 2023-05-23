from typing import Optional
from app.utils.cache_manager import clear_cached_data

# In-memory dictionary to store user sessions
user_sessions = {}


def update_user_session(user_id: int, session_data: Optional[dict]):
    """
    Update the user session data for a given user ID.
    If session_data is None, remove the session for the user.
    """
    if session_data is None:
        user_sessions.pop(user_id, None)
    else:
        user_sessions[user_id] = session_data


def get_user_session(user_id: int) -> Optional[dict]:
    """
    Retrieve the session data for a given user ID.
    Returns None if the user session does not exist.
    """
    return user_sessions.get(user_id)

def cleanup_user_session(user_id: int):
    """
    Clean up any additional session-related data or resources for a given user ID.
    This method can be implemented to handle any necessary cleanup tasks when a user logs out.
    """
    # Get the user session data
    session_data = get_user_session(user_id)

    if session_data:
        # Perform any necessary cleanup tasks based on the session data
        # For example, you can clear any cached data or resources associated with the user session
        cached_data = session_data.get("cached_data")
        if cached_data:
            # Clear the cached data
            clear_cached_data(cached_data)

    # Remove the user session
    update_user_session(user_id, None)
