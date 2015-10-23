# Language Notes
This is a personal repository for languages I have that override the sublime default ones.  Though this repository wasn't meant for public use, all are welcome to use anything found here.  You can file issues if you want, but since I don't view this as a supported repo, I will pick and choose what to fix when I feel like it.

## Fixed and Mods
When using these languages, you can disable the default version of the languages in the Preferences.sublime-settings.

Example:
```javascript
    "ignored_packages":
    [
        "Batch File",
        "C++",
        "Markdown"
    ],
```

### Batch File
- Add Comment support for comment line shortcut

### C/C++/C++11
- Based off of https://github.com/kodLite/cppStartingKit
- Fix comments that trail some preprocessors like #endif etc.

### JSON
- Scope keys different than values so keys can be colored differently than values.

### CSS
- Fix issue where things like (-moz|-o|-ms|-webkit) items would not highlight.
- (-moz|-o|-ms|-webkit) items and properties

### Markdown (Still more to do)
- Add fenced blocks to MultiMarkdown
- MultiMarkdown is the default
- Added Github Flavored Markdown
    - supports fenced blocks
    - added strikedown scoping `markup.strikethrough`
    - adjusted logic for when bold/italic are highlighted
    - emoji scoping for things like `:smile:`.  `markup.emoji`
- Fenced blocks support backticks and tilde supported
- Enable wrapping by default
- Added switcher to choose the default markdown style to use
- ~~Import source highlighting for embedded:~~
    - ~~python~~
    - ~~javascript~~
    - ~~json~~
    - ~~xml~~
    - ~~html~~
    - ~~php~~
    - ~~css~~
    - ~~diff~~
    - ~~perl~~
    - ~~bash~~
    - ~~java~~
    - ~~ini~~
    - ~~apacheconf~~
    - ~~clojure~~
    - ~~ruby~~
    - ~~applescript~~
    - ~~c++/c~~
    - ~~c#~~
    - ~~markdown (experimental)~~
    - ~~batchfile~~
    - ~~erlang~~
    - ~~(more to come)~~

NOTE: Because embedded fences can some times act funny due to import language scoping being too greedy, embedded syntax highlighting has been removed for the time being and possibly forever.

## Colorizing New Scopes

### To Colorize JSON Keys and Python Dictionary Keys ()
Remove this:
```xml
    <dict>
        <key>name</key>
        <string>JSON String</string>
        <key>scope</key>
        <string>meta.structure.dictionary.json string.quoted.double.json</string>
        <key>settings</key>
        <dict>
            <key>foreground</key>
            <string>#CFCFC2</string>
        </dict>
    </dict>
```

Add then add this in its place:
```xml
    <dict>
        <key>name</key>
        <string>Hash String</string>
        <key>scope</key>
        <string>meta.structure.dictionary string</string>
        <key>settings</key>
        <dict>
            <key>foreground</key>
            <string>#E6DB74</string>
        </dict>
    </dict>
    <dict>
        <key>name</key>
        <string>Hash Key String</string>
        <key>scope</key>
        <string>string.quoted.double.key, meta.structure.dictionary.key string</string>
        <key>settings</key>
        <dict>
            <key>foreground</key>
            <string>#66D9EF</string>
        </dict>
    </dict>
```

### To Colorize Function Calls and To Colorize Non-Built-In Function Calls Differently (In Supported Languages)
Add this to theme file:
```xml
    <dict>
        <key>name</key>
        <string>Function Call</string>
        <key>scope</key>
        <string>meta.function-call.generic, meta.function-call.object, meta.function-call.static</string>
        <key>settings</key>
        <dict>
            <key>fontStyle</key>
            <string></string>
            <key>foreground</key>
            <string>#FF80F4</string>
        </dict>
    </dict>
```

### Different Color Background for Fenced Code Blocks and Inline Raw Blocks (If Desired)
You can tweak your theme to have a subtle or dramatic background difference for fenced blocks etc.  Just pick a color that works well for your theme.
```xml
        <dict>
            <key>name</key>
            <string>Markdown Background</string>
            <key>scope</key>
            <string>markup.raw.block.markdown, markup.raw.inline.markdown</string>
            <key>settings</key>
            <dict>
                <key>background</key>
                <string>#262626</string>
            </dict>
        </dict>
```

### Highlight Markdown Lists (This is Not Unique to This Package)
I like lists to be highlighted differently.  This can be done on the default markdown as well.
```xml
        <dict>
            <key>name</key>
            <string>Markdown: List</string>
            <key>scope</key>
            <string>markup.list</string>
            <key>settings</key>
            <dict>
                <key>foreground</key>
                <string>#99CCCC</string>
            </dict>
        </dict>
```

### Highlight Bold, Italic, Strikethrough, Emoji (Github Flavored Only)
```xml
        <dict>
            <key>name</key>
            <string>Markup: Strikethrough</string>
            <key>scope</key>
            <string>markup.strikethrough</string>
            <key>settings</key>
            <dict>
                <key>foreground</key>
                <string>#CC99CC</string>
            </dict>
        </dict>
        <dict>
            <key>name</key>
            <string>Markdown: Bold</string>
            <key>scope</key>
            <string>markup.bold</string>
            <key>settings</key>
            <dict>
                <key>fontStyle</key>
                <string>bold</string>
                <key>foreground</key>
                <string>#CC99CC</string>
            </dict>
        </dict>
        <dict>
            <key>name</key>
            <string>Markup: Italic</string>
            <key>scope</key>
            <string>markup.italic</string>
            <key>settings</key>
            <dict>
                <key>fontStyle</key>
                <string>italic</string>
                <key>foreground</key>
                <string>#CC99CC</string>
            </dict>
        </dict>
        <dict>
            <key>name</key>
            <string>Markup: Emoji</string>
            <key>scope</key>
            <string>markup.emoji</string>
            <key>settings</key>
            <dict>
                <key>background</key>
                <string></string>
                <key>fontStyle</key>
                <string></string>
                <key>foreground</key>
                <string>#F2777A</string>
            </dict>
        </dict>
```
