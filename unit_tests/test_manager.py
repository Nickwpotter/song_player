from manager import Manager
from playlist import PlayList
import pytest

def test_select_or_create_playlist_with_existing_playlists():
    manager = manager.Manager()
    playlist1 = PlayList("Playlist1")
    playlist2 = PlayList("Playlist2")
    manager.playlists = {"Playlist1": playlist1, "Playlist2": playlist2}

    # Simulate user input
    with pytest.raises(SystemExit):
        manager.select_or_create_playlist()

    assert manager.current_playlist in [playlist1, playlist2]

def test_select_or_create_playlist_without_existing_playlists(monkeypatch):
    manager = Manager()

    # Simulate user input for creating a new playlist
    monkeypatch.setattr('builtins.input', lambda x: "NewPlaylist")
    with pytest.raises(SystemExit):
        manager.select_or_create_playlist()

    assert "NewPlaylist" in manager.playlists
    assert manager.current_playlist == manager.playlists["NewPlaylist"]

def test_create_playlist():
    manager = Manager()
    playlist_name = "TestPlaylist"
    manager.create_playlist(playlist_name)

    assert playlist_name in manager.playlists
    assert isinstance(manager.playlists[playlist_name], PlayList)

# You can add more tests as needed

