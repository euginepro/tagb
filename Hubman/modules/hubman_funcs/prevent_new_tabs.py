def get_prevent_new_tabs_script():
    return """
        // Override window.open to do nothing
        window.open = function() {
            console.log('window.open() blocked');
            return window;
        };
        
        // Override target="_blank" links
        document.addEventListener('click', function(e) {
            if (e.target.tagName === 'A' || e.target.closest('a')) {
                const link = e.target.tagName === 'A' ? e.target : e.target.closest('a');
                if (link.target === '_blank' || link.target === '_new') {
                    e.preventDefault();
                    window.location.href = link.href;
                    console.log('Redirected _blank link to current tab:', link.href);
                }
            }
        }, true);
        
        // Block popup windows
        window.addEventListener('beforeunload', function(e) {
            // Allow normal navigation
            return undefined;
        });
        
        // Override other window opening methods
        if (window.showModalDialog) {
            window.showModalDialog = function() {
                console.log('showModalDialog blocked');
                return null;
            };
        }
        console.log('New tab prevention script loaded');
        """
