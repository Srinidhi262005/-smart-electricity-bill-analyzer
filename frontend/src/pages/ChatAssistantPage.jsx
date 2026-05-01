import Chatbot from '../components/Chatbot';

function ChatAssistantPage() {
  return (
    <div className="page-grid">
      <section className="card card-large">
        <h2>Chat Assistant</h2>
        <p>Ask questions in English or Telugu about your bill, usage, or energy savings.</p>
        <Chatbot />
      </section>
    </div>
  );
}

export default ChatAssistantPage;
