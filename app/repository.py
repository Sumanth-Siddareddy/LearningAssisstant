class ResearchRepository:
    def fetch_web_data(self, topic):
        return f"[Web] Deep research content on {topic}."

    def fetch_video_transcripts(self, topic):
        return f"[Video] Transcript analysis on {topic}."

    def fetch_academic_sources(self, topic):
        return f"[Academic] Peer-reviewed content on {topic}."