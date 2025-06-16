class DiaryEntry:
    def __init__(self, title, contents):
        self.title = title
        self.contents = contents
        self.words_read_so_far = 0

    def format(self):
        formatted = f"{self.title} {self.contents}"
        return formatted
    
    def count_words(self):
        words = self.format().split()
        return len(words)
    
    def reading_time(self, wpm):
        total_words = self.count_words()
        minutes = total_words/wpm
        # print(f"Total words counted: {total_words}")
        return minutes
    
# entry = DiaryEntry("My Day", "Today I went to the park and saw some birds.")
# reading_minutes = entry.reading_time(200)
# print(f"Reading time returned: {reading_minutes}")

    def reading_chunk(self, wpm, minutes):

        # Get all the words 
        words_list = self.format().split()

        # Calculate how many words they can read this time
        total_words_can_read = minutes * wpm
        # Figure out where to start reading (using your words_read_so_far)
        chunk = words_list[self.words_read_so_far:self.words_read_so_far + total_words_can_read]
        # Reading chunk should return next chunk - unti contents fully read - if fully read - start from beginning
        if len(chunk) == 0:
            self.words_read_so_far = 0
            chunk = words_list[self.words_read_so_far:self.words_read_so_far + total_words_can_read]
 
        # return a chunk of contents that user can read in string
        result = " ".join(chunk)
        # Update words_read_so_far to include the words we just read
        self.words_read_so_far = self.words_read_so_far + len(chunk)
        return result





    


