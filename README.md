# WipEout HD/Fury Zone Random Color Effects Generator
A little Python script to generate random color effects on WipEout HD/Fury for RPCS3 or Custom Firmware.

# Requirements
<div>
  <p dir="auto">Be sure to have:</p>
  <ul dir="auto">
    <li>
      Python 3.x installed from <a href="https://www.python.org/downloads/">official site</a>
    </li>
    <li>
      <b><i>zonemode.effectsettings</i></b> file (you can extract yours from data00.psarc or get a copy <a href="https://github.com/TheWalkingFroggy/zonerandomizer/blob/main/dummyzonemode.effectsettings">here</a>)
    </li>
  </ul>
</div>

# Usage
<div>
  <p dir="auto">Put both <b><i>randomizer.py</i></b> and <b><i>zonemode.effectsettings</i></b> (renamed as <b><i>dummyzonemode.effectsettings</i></b>) in the same folder. Open Command Prompt:</p>
  <pre>py randomizer.py</pre>
  <p dir="auto">This will generate a new <b><i>zonemode.effectsettings</i></b> file. Paste this in:</p>
  <pre>RPCS3Folder/dev_hdd0/game/NPEA00057(or whatever your region code is)/USRDIR/data/environments</pre>
  <p dir="auto"><b><i>data/environments</i></b> folders probably don't exist. You can create them.</p>
</div>

# Features
<div>
  <ul dir="auto">
    <li>Added support for Zone exclusive tracks (<b><i>Protozo, Mallavol, Corridon 12 and Syncopia</i></b>). However, I don't recommend randomizing them yet as code has been improved only to classic tracks. </li>
    <li>Due to, as name suggests, being a randomizer, it isn't guaranteed you'll receive 'cool to see' colors/effects. Manual editing and adaption is the preffered way for better results.</li>
    <li>The script now is able to add blacks with a current 33% of chance. The randomized colors now have their decimal part decreased from the default of 6 places to just 2 in order to avoid the generation of too much different colors in the       same instruction. However, the output is still formatted with 6 places for a better visual and (eventually) manual editing. <b><i>(ex: 0.871136 -> 0.870000)</i></b>. This may change over time.
    </li>
  </ul>
</div>
