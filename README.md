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
  <p dir="auto">Put both <b><i>randomizer.py</i></b> and <b><i>zonemode.effectsettings</i></b> (renamed as <b><i>dummyzonemode.effectsettings</i></b>) in the same folder. Open CMD:</p>
  <pre>py randomizer.py</pre>
  <p dir="auto">This will generate a new zonemode.effectsettings file. Paste this in:</p>
  <pre>RPCS3Folder/dev_hdd0/game/NPEA00057(or whatever is your region code)/USRDIR/data/environments</pre>
  <p dir="auto"><b><i>data/environments</i></b> folders probably don't exist. You can create them.</p>
</div>

# Limitations
<div>
  <ul dir="auto">
    <li>Currently supports only classic tracks (no <b><i>Protozo, Mallavol, Corridon 12 and Syncopia</i></b>, will add support later).</li>
    <li>Due to, as name suggests, being a randomizer, most likely you won't receive 'cool to see' colors/effects. Manual editing and adaption is the preffered way for better results.</li>
    <li>Code will probably be improved to avoid getting scales of white/grey or too bright colors as they make the track harder to see.</li>
  </ul>
</div>
