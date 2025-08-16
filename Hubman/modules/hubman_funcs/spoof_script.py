def get_spoof_script(n_platform, n_appVersion, n_vendor,n_user_agent, n_language, ram, cores, screen_color_depth, screen_pixel_depth, avail_height,
                     avail_width, width, height,s_webgl, s_renderer, device_name, mac_addr):
    return f"""
    (() => {{
        // === Utilities ===
            const randInt = (min, max) => Math.floor(Math.random() * (max - min + 1)) + min;
            const randFloat = (min, max) => Math.random() * (max - min) + min;
            const randomChoice = (arr) => arr[Math.floor(Math.random() * arr.length)];
            
        // === Universal Chrome Properties (inject platform-specific values) ===
        Object.defineProperty(document, 'hidden', {{ get: () => false }});
        Object.defineProperty(document, 'visibilityState', {{ get: () => 'visible' }});
        Object.defineProperty(navigator, 'platform', {{get: () => '{n_platform}'}});
        Object.defineProperty(navigator, 'oscpu', {{get: () => undefined}});
        Object.defineProperty(navigator, 'appVersion', {{get: () => '{n_appVersion}'}});
        Object.defineProperty(navigator, 'vendor', {{get: () => '{n_vendor}'}});
        Object.defineProperty(navigator, 'userAgent', {{get: () => '{n_user_agent}'}});
        Object.defineProperty(navigator, 'language', {{get: () => '{n_language}'}});
        Object.defineProperty(navigator, 'deviceMemory', {{get: () => {ram}}});
        Object.defineProperty(navigator, 'hardwareConcurrency', {{get: () => {cores}}});
        Object.defineProperty(navigator, 'webdriver', {{get: () => undefined}});

        // === Universal Screen Properties ===
        Object.defineProperty(screen, 'colorDepth', {{get: () => {screen_color_depth}}});
        Object.defineProperty(screen, 'pixelDepth', {{get: () => {screen_pixel_depth}}});
        Object.defineProperty(screen, 'availHeight', {{get: () => {avail_height}}});
        Object.defineProperty(screen, 'availWidth', {{get: () => {avail_width}}});
        Object.defineProperty(screen, 'width', {{get: () => {width} }});
        Object.defineProperty(screen, 'height', {{get: () => {height} }});

        // === Performance API (universal) ===
        if (window.performance && window.performance.memory) {{
            Object.defineProperty(performance.memory, 'usedJSHeapSize', {{
                get: () => Math.floor(Math.random() * 50000000) + 10000000
            }});
            Object.defineProperty(performance.memory, 'totalJSHeapSize', {{
                get: () => Math.floor(Math.random() * 100000000) + 50000000
            }});
            Object.defineProperty(performance.memory, 'jsHeapSizeLimit', {{
                get: () => {ram * 1024 * 1024 * 1024}
            }});
        }}

        // === Plugin and MimeType Spoofing (universal Chrome) ===
        Object.defineProperty(navigator, 'plugins', {{
            get: () => {{
                const plugins = [
                    {{name: 'Chrome PDF Plugin', filename: 'internal-pdf-viewer', description: 'Portable Document Format'}},
                    {{name: 'Chromium PDF Plugin', filename: 'internal-pdf-viewer', description: 'Portable Document Format'}},
                    {{name: 'Microsoft Edge PDF Plugin', filename: 'internal-pdf-viewer', description: 'Portable Document Format'}},
                    {{name: 'PDF Viewer', filename: 'internal-pdf-viewer', description: 'Portable Document Format'}},
                    {{name: 'Chrome PDF Viewer', filename: 'internal-pdf-viewer', description: 'Portable Document Format'}}
                ];
                plugins.namedItem = function(name) {{ return this.find(p => p.name === name) || null; }};
                return plugins;
            }}
        }});

        Object.defineProperty(navigator, 'mimeTypes', {{
            get: () => {{
                const mimeTypes = [
                    {{type: 'application/pdf', suffixes: 'pdf', description: 'Portable Document Format'}},
                    {{type: 'text/pdf', suffixes: 'pdf', description: 'Portable Document Format'}}
                ];
                mimeTypes.namedItem = function(name) {{ return this.find(m => m.type === name) || null; }};
                return mimeTypes;
            }}
        }});

        // === WebRTC Complete Blocking (universal) ===
        Object.defineProperty(window, 'RTCPeerConnection', {{get: () => undefined}});
        Object.defineProperty(window, 'webkitRTCPeerConnection', {{get: () => undefined}});
        Object.defineProperty(window, 'mozRTCPeerConnection', {{get: () => undefined}});

        const _getParameter = WebGLRenderingContext.prototype.getParameter;
        WebGLRenderingContext.prototype.getParameter = function(param) {{
            try {{
                const ext = this.getExtension("WEBGL_debug_renderer_info");
                if (ext) {{
                    if (param === ext.UNMASKED_VENDOR_WEBGL) return "{s_webgl}";
                    if (param === ext.UNMASKED_RENDERER_WEBGL) return "{s_renderer}";
                }}
            }} catch (e) {{}}
            return _getParameter.call(this, param);
        }};
        
        if (window.WebGL2RenderingContext) {{
            const _getParameter2 = WebGL2RenderingContext.prototype.getParameter;
            WebGL2RenderingContext.prototype.getParameter = function(param) {{
                try {{
                    const ext = this.getExtension("WEBGL_debug_renderer_info");
                    if (ext) {{
                        if (param === ext.UNMASKED_VENDOR_WEBGL) return "{s_webgl}";
                        if (param === ext.UNMASKED_RENDERER_WEBGL) return "{s_renderer}";
                    }}
                }} catch (e) {{}}
                return _getParameter2.call(this, param);
            }};
        }}
        
        // === Font Detection Interference (universal) ===
        const _createElement = document.createElement;
        document.createElement = function(tagName) {{
            const element = _createElement.call(this, tagName);
            if (tagName.toLowerCase() === 'canvas') {{
                const _getContext = element.getContext;
                element.getContext = function(contextType) {{
                    const context = _getContext.call(this, contextType);
                    if (contextType === '2d' && context) {{
                        const _measureText = context.measureText;
                        context.measureText = function(text) {{
                            const metrics = _measureText.call(this, text);
                            metrics.width += (Math.random() - 0.5) * 0.1;
                            return metrics;
                        }};
                    }}
                    return context;
                }};
            }}
            return element;
        }};

        // === Remove Automation Indicators (universal Chrome) ===
        delete window.cdc_adoQpoasnfa76pfcZLmcfl_Array;
        delete window.cdc_adoQpoasnfa76pfcZLmcfl_Promise;
        delete window.cdc_adoQpoasnfa76pfcZLmcfl_Symbol;
        delete window.cdc_adoQpoasnfa76pfcZLmcfl_JSON;
        delete window.cdc_adoQpoasnfa76pfcZLmcfl_Object;
        Object.defineProperty(window, 'outerHeight', {{get: () => window.innerHeight}});
        Object.defineProperty(window, 'outerWidth', {{get: () => window.innerWidth}});
        
        // === WebGPU Spoof ===
            if ('gpu' in navigator) {{
              Object.defineProperty(navigator.gpu, 'adapter', {{
                get: () => ({{
                  features: new Set(['texture-compression-bc']),
                  limits: {{}},
                  isSoftware: false,
                  name: ' ',
                  vendor: '{n_vendor}',
                  architecture: 'Unknown',
                }})
              }});
            }}
            
            // === Media Devices: spoof enumerateDevices to add noise ===
            if (navigator.mediaDevices && navigator.mediaDevices.enumerateDevices) {{
                const originalEnum = navigator.mediaDevices.enumerateDevices;
                navigator.mediaDevices.enumerateDevices = function() {{
                    return originalEnum.call(this).then(devices => {{
                        devices.forEach(d => {{
                            if (typeof d.deviceId === 'string' && d.deviceId.length > 0) {{
                                d.deviceId = d.deviceId.slice(0, 8) + Math.random().toString(36).slice(2, 6);
                            }}
                            if (typeof d.groupId === 'string' && d.groupId.length > 0) {{
                                d.groupId = d.groupId.slice(0, 8) + Math.random().toString(36).slice(2, 6);
                            }}
                        }});
                        return devices;
                    }});
                }};
            }}
            
            // === ClientRects noise ===
            const _getClientRects = Element.prototype.getClientRects;
            Element.prototype.getClientRects = function() {{
              const rects = _getClientRects.apply(this);
              for (let i = 0; i < rects.length; i++) {{
                rects[i] = new DOMRect(
                  rects[i].x + (Math.random() - 0.5) * 0.5,
                  rects[i].y + (Math.random() - 0.5) * 0.5,
                  rects[i].width + (Math.random() - 0.5) * 0.5,
                  rects[i].height + (Math.random() - 0.5) * 0.5
                );
              }}
              return rects;
            }};
            
            // === SpeechSynthesis Voices noise ===
            if (window.speechSynthesis && window.speechSynthesis.getVoices) {{
              const originalGetVoices = window.speechSynthesis.getVoices;
              window.speechSynthesis.getVoices = function() {{
                let voices = originalGetVoices.call(this);
                voices.push(new SpeechSynthesisVoice({{
                  name: 'Voice ' + Math.floor(Math.random() * 1000),
                  lang: 'en-US',
                  voiceURI: ' ',
                  localService: true,
                  default: false
                }}));
                return voices;
              }};
            }}
            
            // === Device Name Spoof ===
            Object.defineProperty(navigator, 'deviceName', {{
              get: () => '{device_name}'
            }});
            
            // === MAC Address Spoof ===
            Object.defineProperty(navigator, 'macAddress', {{
              get: () => '{mac_addr}'
            }});
            
            // === Enable Port Scan Protection ===
            const _WebSocket = window.WebSocket;
            window.WebSocket = function(url, protocols) {{
              if (typeof url === 'string' && url.startsWith('ws://localhost')) {{
                throw new Error('Blocked suspicious WebSocket connection');
              }}
              return new _WebSocket(url, protocols);
            }};
        
            // === Canvas Spoof ===
            const randIntCanvas = () => Math.floor(Math.random() * 10 - 5);
            const randFloatCanvas = () => Math.random() * 0.00001;
            
            const _getContext = HTMLCanvasElement.prototype.getContext;
            HTMLCanvasElement.prototype.getContext = function(contextType, contextAttributes) {{
                if (contextType === '2d') {{
                    contextAttributes = contextAttributes || {{}};
                    contextAttributes.willReadFrequently = true;
                }}
                return _getContext.call(this, contextType, contextAttributes);
            }};
        
            const _toDataURL = HTMLCanvasElement.prototype.toDataURL;
            HTMLCanvasElement.prototype.toDataURL = function() {{
                const ctx = this.getContext('2d');
                const imgData = ctx.getImageData(0, 0, this.width, this.height);
                for (let i = 0; i < imgData.data.length; i += 4) {{
                    imgData.data[i] += randIntCanvas();     // R
                    imgData.data[i+1] += randIntCanvas();   // G
                    imgData.data[i+2] += randIntCanvas();   // B
                    imgData.data[i+3] += randIntCanvas();   // A
                }}
                ctx.putImageData(imgData, 0, 0);
                return _toDataURL.apply(this, arguments);
            }};
        
            const _getImageData = CanvasRenderingContext2D.prototype.getImageData;
            CanvasRenderingContext2D.prototype.getImageData = function(...args) {{
                const imgData = _getImageData.apply(this, args);
                for (let i = 0; i < imgData.data.length; i += 4) {{
                    imgData.data[i] += randIntCanvas();
                    imgData.data[i+1] += randIntCanvas();
                    imgData.data[i+2] += randIntCanvas();
                    imgData.data[i+3] += randIntCanvas();
                }}
                return imgData;
            }};
        
            // === AudioContext Spoof ===
            const _getChannelData = AudioBuffer.prototype.getChannelData;
            AudioBuffer.prototype.getChannelData = function() {{
                const data = _getChannelData.apply(this, arguments);
                const copy = new Float32Array(data.length);
                for (let i = 0; i < data.length; i++) {{
                    copy[i] = data[i] + randFloatCanvas();
                }}
                return copy;
            }};
        
            
            const _getShaderPrecisionFormat = WebGLRenderingContext.prototype.getShaderPrecisionFormat;
            WebGLRenderingContext.prototype.getShaderPrecisionFormat = function() {{
                return {{ rangeMin: 127, rangeMax: 127, precision: 6 }};
            }};
        
            // === WebGL readPixels noise injection ===
            const _readPixels = WebGLRenderingContext.prototype.readPixels;
            WebGLRenderingContext.prototype.readPixels = function(x, y, w, h, format, type, pixels) {{
                _readPixels.call(this, x, y, w, h, format, type, pixels);
                if (pixels && pixels.length) {{
                    for (let i = 0; i < pixels.length; i++) {{
                        pixels[i] = pixels[i] ^ (Math.floor(Math.random() * 2)); // slight XOR noise
                    }}
                }}
            }};
            
            console.log("ended spoofff");
            
    }})();
    """