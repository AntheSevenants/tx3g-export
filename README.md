# tx3g-export
Exporting tx3g subtitles from QuickTime MOV files

This repository details my method for exporting subtitles from prehistoric mov files. These subtitles are so-called "TX3G" subtitles. While there are a number of options for converting these subtitles (e.g. using ffmpeg or MP4box), all these options implode when you're dealing with "foreign" (from an Anglo perspective) characters. For example:

```
ffmpeg -y -sub_charenc "MAC" -i "file.mov" -map 0:s:0 QT-subtitles.srt
```

...results in...

```srt
2
00:00:08,880 --> 00:00:09,882
<font size="0" color="#001200">{\an7}¿Qué haces despiert</font>
```

ffmpeg drops the final characters of this subtitle line (`a?`). This is bad. If you don't have special characters, try using ffmpeg anyway! Maybe it works for subtitle files without special characters...

MP4box refuses to export TX3G files with foreign characters when SRT export is specified. Exports to TTXT work, but lines containing foreign characters are blanked out:

```xml
<TextSample sampleTime="00:00:08.880" sampleDescriptionIndex="1" xml:space="preserve"></TextSample>
```

The only reliable way to export subtitles with foreign characters that I've found is to use... [QuickTime Pro 7](https://www.videohelp.com/software/Quicktime-Pro). I know. To make matters worse, you need a *licence* to export subtitles in QuickTime. Because QuickTime Pro can be considered abandonware at this point in time, I think it's fair to find a serial key online. There is no online activation, so Apple will never have to know...

Another downside to having to use QuickTime Pro is that there is no way to automate batch conversion. This means you'll have to manually export every single file you have. I only have a moderate number of files (~ 50), but if you have thousands of files, you'll be spending a lot of time clicking...

## Step 1: Exporting subtitles to QuickTime TeXML

Anyway, here's how to export the subtitles to the QuickTime TeXML format. 

1. Open your file in QuickTime Pro.  
	![QuickTime Pro](https://user-images.githubusercontent.com/84721952/186732162-bc169895-2faa-426f-8825-a4f81892bcbf.png)
2. Press File > Export.
3. Under "Export", select "Text to QuickTime TeXML".  
	![QuickTime Pro export dialog](https://user-images.githubusercontent.com/84721952/186732200-b95e3981-3973-4b7c-b0a7-916f88e831b3.png)
4. You now have a QuickTime TeXML file.

(If you have multiple subtitle streams, QuickTime will only export the first one. To export a non-first subtitle stream, press Window > Movie Properties, click the desired subtitle stream in the menu, then click the 'Extract' button. A new window will pop up with *only* the subtitles. You can now follow along again from Step 2.)

(If QuickTime crashes upon opening your video, try re-encoding it with ffmpeg first. Yes, I know this is getting ridiculous. This is the command you need:

```
ffmpeg -y -i input.mov -scodec copy -map 0 output.mov
```

This command will retain *all* subtitle streams (not just the first one -- seriously, why does all software default to throwing other streams away?)  
)

This would actually be a usable format, but unfortunately the subtitle duration is measured in some format I don't understand:
```xml
<sample duration="601" keyframe="true">
	<description horizontalJustification="Center" verticalJustification="Top"
 backgroundColor="100%, 100%, 100%, 100%" format="tx3g">
		<defaultTextBox width="320" height="38"></defaultTextBox>
		<fontTable>
			<font id="1" name="Geneva"></font>
		</fontTable>
		<sharedStyles>
			<style id="1">{font-table: 1}{font-size: 14}{font-style: normal}{font-weight: normal}{text-decoration: normal}{color: 0%, 
0%, 0%, 100%}</style>
		</sharedStyles>
	</description>
	<sampleData targetEncoding="utf8">
		<text styleID="1">¿Qué haces despierta?</text>
	</sampleData>
</sample>
```
*601: what does it mean?*

## Step 2: Exporting subtitles to TTXT

Fortunately, we can use the borked TTXT format as a basis for our "true" subtitle file. Even though the lines containing foreign characters are blanked out, the *order* of the subtitles corresponds to that of the QuickTime TeXML. To export to a TTXT file with MP4box:

1. First, we have to find out what the ID is of the subtitle track. You can find this by using the following command:  
	`mp4box -info "file.mov"`

```
# Track 3 Info - ID 4 - TimeScale 600
Media Duration 00:00:48.720
Track has 1 edits: track duration is 00:00:48.720
Track flags: Enabled In Movie In Preview Size is AspectRatio
Media Info: Language "Undetermined (und)" - Type "text:text" - 23 samples
1 UDTA types:
        name: spaans
Unknown Text Stream
        Size 320 x 36 - Translation X=0 Y=240 - Layer -1
        RFC6381 Codec Parameters: text
        All samples are sync
        Max sample duration: 5328 / 600
```
2. From the output, we can see that the subtitle has track ID 4 (not track ID 3, don't be confused!)
2. Now, convert the embedded subtitles with the following command:  
	`mp4box "file.mov" -ttxt 4` (`4` is the ID of the subtitle track)
3. You now get your (borked) TTXT file as an output in the directory of the MOV file.

## Step 3: Putting TeXML and TTXT together

We could now start manually copying and pasting subtitle contents from the TeXML file to the TTXT file. This is tedious work, however, and would result in copy-paste errors, RSI and mental insanity. Luckily, I put together a Python script which can automate this process for you. You can use it as follows:

0. Clone this repository.
1. Install all dependencies:  
	`pip install -r requirements.txt`
1. `python texml2ttxt.py texml.xml ttxt_in.ttxt ttxt_out.ttxt`

Your TeXML and TTXT files will be merged, and the resulting output will be saved as ttxt_out.ttxt (or whatever you decide on as the output filename).

### BONUS: bulk conversion

If you a bunch of files, you can first do step 1 for all files, then step 2 for all files. Once you have collected both your TeXML and TTXT files, put them both in separate directories. For example:
- all TeXML files in a directory `source_tx3g`
- all TTXT files in a directory `source_ttxt`

Now you can use my special bulk conversion version of the script to combine your files in bulk. **Make sure that they have the same base names:** for example, `movie.xml` and `movie.ttxt`. The script won't know what files to put together if they have different names! Syntax is as follows:

```
python texml2ttxt_bulk.py source_tx3g source_txtt out
```

(with `out` being the output directory for your files)

## Step 4: To SRT and beyond

You can now use MP4box again to export the TTXT file to another file format, such as SRT.

```
mp4box -srt "ttxt_out.ttxt"
```

This will *finally* produce the output we originally hoped to get using ffmpeg.

![Final SRT loaded in MPC-BE](https://user-images.githubusercontent.com/84721952/186733060-fc7c0a93-f645-4ba3-90b5-1efd30344200.png)

### BONUS: bulk conversion

If you used the bulk conversion script to combine the TeXML and TTXT files, you probably also want to bulk convert the resulting TTXT files to SRT. Don't worry. I've got you covered. You need MP4box installed on your machine, and callable from anywhere (its install directory needs to be in your environment). This command takes all TTXT files from `out` and exports them to SRT. These will end up in the `srt` directory.

```
python ttxt2srt.py out srt
```

Finally, sweet automation!