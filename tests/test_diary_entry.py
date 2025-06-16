from lib.diary_entry import DiaryEntry  

def test_diary_entry_initialization():
    title = "Test Title"
    contents = "This is the content of the diary entry."
    entry = DiaryEntry(title, contents)
    assert entry.title == title
    assert entry.contents == contents

def test_diary_entry_format():
    title = "My Title:"
    contents = "These are the contents"
    entry = DiaryEntry(title, contents)
    result = entry.format()
    expected = "My Title: These are the contents"
    assert result == expected

def test_count_words_in_diary_entry():
    title = "My day:"
    contents = "I had a fun day"
    entry = DiaryEntry(title, contents)
    result = entry.count_words()
    expected = 7
    assert result == expected 

def test_reading_time():
    title = "My day:"
    contents = "I had a fun day. I'm Very happy."
    entry = DiaryEntry(title, contents)
    wpm = 100
    # Calculate expected minutes
    expected_minutes = 0.1
    # Call reading_time(wpm)
    result = entry.reading_time(100)
    assert result == expected_minutes

def test_reading_chunk_returns_first_chunk():
    # Create a diary entry with known content
    entry = DiaryEntry("Day", "I went to the park today and played football with")
    # Call reading_chunk with specific wpm and minutes
    result = entry.reading_chunk(3, 1)  # Can read 3 words in 1 minute
    # Assert that it returns the expected first chunk
    expected = "Day I went"
    assert result == expected

def test_reading_chunk_returns_second_chunk():
    # Create a diary entry with known content
    entry = DiaryEntry("Day", "I went to the park today and played football with friends.")
    # Call reading_chunk once to read first chunk
    result = entry.reading_chunk(3,1)
    # Call reading_chunk again
    result = entry.reading_chunk(3,1)
    # Assert that it returns the expected second chunk
    expected = "to the park"
    assert result == expected

def test_reading_chunk_restarts_after_reading_all():
    # Create a diary entry with known content
    entry = DiaryEntry("Day", "I went to the park today and played football with friends.")
    # Call reading_chunk enough times to read everything
    result = entry.reading_chunk(3,1)
    result = entry.reading_chunk(3,1)
    result = entry.reading_chunk(3,1)
    result = entry.reading_chunk(3,1)
    # Call reading_chunk one more time
    result = entry.reading_chunk(3,1)
    # Assert that it restarts from the beginning
    expected = "Day I went"
    assert result == expected
    pass