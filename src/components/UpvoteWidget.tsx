import React, { useEffect, useState } from 'react';

export default function UpvoteWidget({ userId, email }: { userId?: string, email?: string }) {
  const [remountKey, setRemountKey] = useState(0);

  useEffect(() => {
    // Force hard remount for cleanup when identity changes
    setRemountKey(k => k + 1);
    
    // Proactive cleanup of existing floating elements
    // @ts-ignore
    if (window.__upvote_cleanup) window.__upvote_cleanup();
  }, [userId, email]);

  return (
    <div key={remountKey}>
      <div className="upvote-widget"
           data-application-id="69b6c4e6f244031d81ca6da6"
           data-user-id={userId || ''}
           data-email={email || ''}
           data-position="right"
           data-theme="light"
           data-logo-url="/logo.png"         
           data-product-overview="..."       
           data-about-text="..."             
           data-faqs='[{"question":"Q?","answer":"A."}]'>
      </div>
      <script src="https://upvote.entrext.com/widget.js" async />
    </div>
  );
}
