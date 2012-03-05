# Language Notes

## Fixed and Mods
When using these languages, you can disable the default version of the languages in the Preferences.sublime-settings.

Example:

    "ignored_packages":
    [
        "Python",
        "Batch File",
        "JavaScript",
        "Perl",
        "C++",
        "PHP"
    ],

### Javascript
- Fix some function related highlighting bugs
- Add scope for targeting function calls that are not system function calls

### JSON
- Add sublime-commands to file types
- Give finer granularity with string types in JSON.  Key strings have special scope.

### Batch File
- Add Comment support for comment line shortcut

### C++
- Fix #define regex to work more reliably
- Fix comments that trail some preprocessors like #endif etc.
- Fix sizeof scope not getting set properly
- Add scope for targeting function calls that are not system function calls

### Perl
- Comment out regex that targets ```<<``` and breaks code it using bitwise ```<<``` operand
- Add support for scoping flags of match regex ```m/regex/egimos```

### PHP
- Add scope for targeting function calls that are not system function calls

### Python
- Add scope for targeting function calls that are not system function calls
- Ensure that dot function calls do not scope all parent memebers, but just the function call

## Colorizing New Scopes

### To Colorize JSON Keys and Python Dictionary Keys ()
Remove this:

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

Add then add this in its place:

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

### To Colorize Function Calls and To Colorize Non-Built-In Function Calls Differently (In Supported Languages)
Add this to theme file:

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
