#!/usr/bin/env python3
import sys
import os
import gi
import webbrowser
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
gi.require_version('Notify', '0.7')
from gi.repository import Gtk,Gio, Gdk, Notify
import subprocess
class MainWindow(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        menu = Gio.Menu.new()
        # Encryption and decryption submenu
        encryption_decryption_menu = Gio.Menu.new()
        menu.append_submenu("Encryption & Decryption", encryption_decryption_menu)

        # Create the submenu actions for Encryption & Decryption
        cyberchef_action = Gio.MenuItem.new("Cyber Chef", "win.cyberchef")
        rot13_action = Gio.MenuItem.new("Rot13", "win.rot13")
        decode_action = Gio.MenuItem.new("Decode", "win.decode")
        encode_action = Gio.MenuItem.new("Encode-Decode", "win.encode")
        encryption_decryption_menu.append_item(cyberchef_action)
        encryption_decryption_menu.append_item(rot13_action)
        encryption_decryption_menu.append_item(decode_action)
        encryption_decryption_menu.append_item(encode_action)
        
        #End of Encryption and decryption submenu
        #Web tools submenu
        web_tools_menu = Gio.Menu.new()
        menu.append_submenu("Web Tools", web_tools_menu)
        
        #Create the submenu actions for Web Tools
        urlscan_action = Gio.MenuItem.new("Urlscan.io", "win.urlscan")
        vulnhub_action = Gio.MenuItem.new("Vulnhub", "win.vulnhub")
        opswat_action = Gio.MenuItem.new("OPSWAT", "win.opswat")
        exploitdb_action = Gio.MenuItem.new("ExploitDB", "win.exploitdb")
        web_tools_menu.append_item(urlscan_action)
        web_tools_menu.append_item(vulnhub_action)
        web_tools_menu.append_item(opswat_action)
        web_tools_menu.append_item(exploitdb_action)
        #End of Web tools submenu
        
        #software submenu
        software_menu = Gio.Menu.new()
        menu.append_submenu("Software Tools", software_menu)
        #software submenus some 
        informationgathering_submenu = Gio.Menu.new()
        vulnerabilityanalysis_submenu = Gio.Menu.new()
        webapplictionanalysis_submenu = Gio.Menu.new()
        databaseassessment_submenu = Gio.Menu.new()
        passwordattacks_submenu = Gio.Menu.new()
        wirelessattacks_submenu = Gio.Menu.new()
        reverseengineering_submenu = Gio.Menu.new()
        explorationtools_submenu = Gio.Menu.new()
        sniffingtools_submenu = Gio.Menu.new()
        postexploitation_submenu = Gio.Menu.new()
        forensics_submenu = Gio.Menu.new()
        reportingtools_submenu = Gio.Menu.new()
        socialengineeringtoolkit_submenu = Gio.Menu.new()
        systemservicestoolkit_submenu = Gio.Menu.new()
        

        software_menu.append_submenu("Information Gathering", informationgathering_submenu)
        software_menu.append_submenu("Vulnerability Analysis", vulnerabilityanalysis_submenu)
        software_menu.append_submenu("Web Application Analysis", webapplictionanalysis_submenu)
        software_menu.append_submenu("Data Base Assessment", databaseassessment_submenu)
        software_menu.append_submenu("Password Attacks", passwordattacks_submenu)
        software_menu.append_submenu("Wireless Attacks", wirelessattacks_submenu)
        software_menu.append_submenu("Reverse Engineering", reverseengineering_submenu)
        software_menu.append_submenu("Exploration Tools", explorationtools_submenu)
        software_menu.append_submenu("Sniffing Tools",sniffingtools_submenu)
        software_menu.append_submenu("Post Exploitation",postexploitation_submenu)
        software_menu.append_submenu("Forensics",forensics_submenu)
        software_menu.append_submenu("Reporting Tools",reportingtools_submenu)
        software_menu.append_submenu("Social Engineering Toolkit", socialengineeringtoolkit_submenu)
        software_menu.append_submenu("System Services Toolkit",systemservicestoolkit_submenu)
        
        # software sub InformationGathering submenus
        
        # Information Gathering submenu
        amass_action = Gio.MenuItem.new("Amass", "win.Amass")
        dmitry_action = Gio.MenuItem.new("Dmitry", "win.Dmitry")
        ikescan_action = Gio.MenuItem.new("Ike-Scan", "win.Ikescan")
        legionroot_action = Gio.MenuItem.new("legion(root)", "win.Legionroot")
        matelgo_action = Gio.MenuItem.new("Matelgo", "win.Matelgo")
        netdiscover_action = Gio.MenuItem.new("Netdiscover", "win.Netdiscover")
        nmap_action = Gio.MenuItem.new("Nmap", "win.Nmap")
        reconng_action = Gio.MenuItem.new("Recon-ng", "win.Reconng")
        spiderfoot_action = Gio.MenuItem.new("Spider Foot", "win.Spiderfoot")

        informationgathering_submenu.append_item(amass_action)
        informationgathering_submenu.append_item(dmitry_action)
        informationgathering_submenu.append_item(ikescan_action)
        informationgathering_submenu.append_item(legionroot_action)
        informationgathering_submenu.append_item(matelgo_action)
        informationgathering_submenu.append_item(netdiscover_action)
        informationgathering_submenu.append_item(nmap_action)
        informationgathering_submenu.append_item(reconng_action)
        informationgathering_submenu.append_item(spiderfoot_action)

        # Vulnerability Analysis submenu
        gvmintalsetup_action = Gio.MenuItem.new("GVM Intal Setup", "win.Gvmintalsetup")
        gvmstart_action = Gio.MenuItem.new("GVM Start", "win.Gvmstart")
        legionroot_action = Gio.MenuItem.new("legion(root)", "win.Legionroot")
        lynis_action = Gio.MenuItem.new("Lynis", "win.Lynis")
        nikito_action = Gio.MenuItem.new("Nikito", "win.Nikito")
        nmap_action = Gio.MenuItem.new("Nmap", "win.Nmap")
        peass_action = Gio.MenuItem.new("Peass", "win.Peass")
        unixprvesccheck_action = Gio.MenuItem.new("unix-privesc-check", "win.Unixprvesccheck")

        vulnerabilityanalysis_submenu.append_item(gvmintalsetup_action)
        vulnerabilityanalysis_submenu.append_item(gvmstart_action)
        vulnerabilityanalysis_submenu.append_item(legionroot_action)
        vulnerabilityanalysis_submenu.append_item(lynis_action)
        vulnerabilityanalysis_submenu.append_item(nikito_action)
        vulnerabilityanalysis_submenu.append_item(nmap_action)
        vulnerabilityanalysis_submenu.append_item(peass_action)
        vulnerabilityanalysis_submenu.append_item(unixprvesccheck_action)

        # Web Application Analysis submenu
        burpsuite_action = Gio.MenuItem.new("Burp Suite", "win.burpsuite")
        commix_action = Gio.MenuItem.new("Commix", "win.commix")
        httrack_action = Gio.MenuItem.new("HT-Track", "win.httrack")
        pros_action = Gio.MenuItem.new("Prox", "win.prox")
        skipfish_action = Gio.MenuItem.new("Skipfish", "win.skipfish")
        sqlmap_action = Gio.MenuItem.new("SQLmap", "win.sqlmap")
        webscrab_action = Gio.MenuItem.new("Web Scrab", "win.webscrab")
        webshells_action = Gio.MenuItem.new("Web Shells", "win.webshells")
        wpscan_action = Gio.MenuItem.new("WPScan", "win.wpscan")
        zap_action = Gio.MenuItem.new("ZAP", "win.zap")
        
        webapplictionanalysis_submenu.append_item(burpsuite_action)
        webapplictionanalysis_submenu.append_item(commix_action)
        webapplictionanalysis_submenu.append_item(httrack_action)
        webapplictionanalysis_submenu.append_item(pros_action)
        webapplictionanalysis_submenu.append_item(skipfish_action)
        webapplictionanalysis_submenu.append_item(sqlmap_action)
        webapplictionanalysis_submenu.append_item(webscrab_action)
        webapplictionanalysis_submenu.append_item(webshells_action)
        webapplictionanalysis_submenu.append_item(wpscan_action)
        webapplictionanalysis_submenu.append_item(zap_action)
        
        #Database Attacks submenu
        jsqlinjection_action = Gio.MenuItem.new("JSQL Injection", "win.jsqlinjection")
        mdbsql_action = Gio.MenuItem.new("MDB-SQL", "win.mdb-sql")
        oscanner_action = Gio.MenuItem.new("Oscanner", "win.oscanner")
        sidegueuser_action = Gio.MenuItem.new("Sidegueuser", "win.sidegueuser")
        sqldict_action = Gio.MenuItem.new("SQLdict", "win.sqldict")
        sqllitedbbrowser_action = Gio.MenuItem.new("SQLlite DB Browser", "win.sqllitedbbrowser")
        sqlmap_action = Gio.MenuItem.new("SQLmap", "win.sqlmap")
        sqlninja_action = Gio.MenuItem.new("SQLninja", "win.sqlninja")
        sqlsus_action = Gio.MenuItem.new("SQLsus", "win.sqlsus")
        transcmdlog_action = Gio.MenuItem.new("Transcmdlog", "win.transcmdlog")
        
        databaseassessment_submenu.append_item(jsqlinjection_action)
        databaseassessment_submenu.append_item(mdbsql_action)
        databaseassessment_submenu.append_item(oscanner_action)
        databaseassessment_submenu.append_item(sidegueuser_action)
        databaseassessment_submenu.append_item(sqldict_action)
        databaseassessment_submenu.append_item(sqllitedbbrowser_action)
        databaseassessment_submenu.append_item(sqlmap_action)
        databaseassessment_submenu.append_item(sqlninja_action)
        databaseassessment_submenu.append_item(sqlsus_action)
        databaseassessment_submenu.append_item(transcmdlog_action)
        
        # Password Attacks submenu
        cewl_action = Gio.MenuItem.new("Cewl", "win.cewl")
        crunch_action = Gio.MenuItem.new("Crunch", "win.crunch")
        hashcat_action = Gio.MenuItem.new("Hashcat", "win.hashcat")
        hydra_action = Gio.MenuItem.new("Hydra", "win.hydra")
        john_action = Gio.MenuItem.new("John", "win.john")
        johnny_action = Gio.MenuItem.new("Johnny", "win.johnny")
        medusa_action = Gio.MenuItem.new("Medusa", "win.medusa")
        nrcrack_action = Gio.MenuItem.new("Ncrack", "win.ncrack")
        ophcrack_action = Gio.MenuItem.new("Ophcrack", "win.ophcrack")
        ranbowcrack_action = Gio.MenuItem.new("Rainbow Crack", "win.rainbowcrack")
        rcrackimt_action = Gio.MenuItem.new("Rcracki Mt", "win.rcrackimt")
        wordlists_action = Gio.MenuItem.new("Wordlists", "win.wordlists")
        
        passwordattacks_submenu.append_item(cewl_action)
        passwordattacks_submenu.append_item(crunch_action)
        passwordattacks_submenu.append_item(hashcat_action)
        passwordattacks_submenu.append_item(hydra_action)
        passwordattacks_submenu.append_item(john_action)
        passwordattacks_submenu.append_item(johnny_action)
        passwordattacks_submenu.append_item(medusa_action)
        passwordattacks_submenu.append_item(nrcrack_action)
        passwordattacks_submenu.append_item(ophcrack_action)
        passwordattacks_submenu.append_item(ranbowcrack_action)
        passwordattacks_submenu.append_item(rcrackimt_action)
        passwordattacks_submenu.append_item(wordlists_action)
        
        # Wireless Attacks submenu
        aircrackng_action = Gio.MenuItem.new("Aircrack-ng", "win.aircracking")
        airmonng_action = Gio.MenuItem.new("Airmon-ng", "win.airmon")
        chrip_action = Gio.MenuItem.new("Chirp", "win.chirp")
        covpatty_action = Gio.MenuItem.new("Covpatty", "win.covpatty")
        fernwificracker_action = Gio.MenuItem.new("Fern Wifi Cracker", "win.fern")
        gprx_action = Gio.MenuItem.new("GPRX", "win.gprx")
        kismet_action = Gio.MenuItem.new("Kismet", "win.kismet")
        mdk3_action = Gio.MenuItem.new("MDK3", "win.mdk3")
        mfoc_action = Gio.MenuItem.new("MFoc", "win.mfoc")
        mfterm_action = Gio.MenuItem.new("MFterm", "win.mfterm")
        pixiwps_action = Gio.MenuItem.new("PixiWPS", "win.pixiwps")
        rever_action = Gio.MenuItem.new("Rever", "win.rever")
        wifite_action = Gio.MenuItem.new("Wifite", "win.wifite")
        
        wirelessattacks_submenu.append_item(aircrackng_action)
        wirelessattacks_submenu.append_item(airmonng_action)
        wirelessattacks_submenu.append_item(chrip_action)
        wirelessattacks_submenu.append_item(covpatty_action)
        wirelessattacks_submenu.append_item(fernwificracker_action)
        wirelessattacks_submenu.append_item(gprx_action)
        wirelessattacks_submenu.append_item(kismet_action)
        wirelessattacks_submenu.append_item(mdk3_action)
        wirelessattacks_submenu.append_item(mfoc_action)
        wirelessattacks_submenu.append_item(mfterm_action)
        wirelessattacks_submenu.append_item(pixiwps_action)
        wirelessattacks_submenu.append_item(rever_action)
        wirelessattacks_submenu.append_item(wifite_action)
        
        # Reverse Engineering submenu
        apktool_action = Gio.MenuItem.new("Apktool", "win.apktool")
        bytecodeviewr_action = Gio.MenuItem.new("Bytecode Viewer", "win.bytecodeviewer")
        clang_action = Gio.MenuItem.new("Clang", "win.clang")
        clangplus_action = Gio.MenuItem.new("Clang++", "win.clang++")
        cutter_action = Gio.MenuItem.new("Cutter", "win.cutter")
        dex2jar_action = Gio.MenuItem.new("Dex2Jar", "win.dex2jar")
        edbdebugger_action = Gio.MenuItem.new("Edb Debugger", "win.edbdebugger")
        ghidra_action = Gio.MenuItem.new("Ghidra", "win.ghidra")
        jadxgui_action = Gio.MenuItem.new("Jadx Gui", "win.jadxgui")
        javasnoop_action = Gio.MenuItem.new("Java Snoop", "win.javasnoop")
        jdgui_action = Gio.MenuItem.new("JD Gui", "win.jdgui")
        NASMSHELL_action = Gio.MenuItem.new("NASM Shell", "win.nasmshell")
        ollydbg_action = Gio.MenuItem.new("Ollydbg", "win.ollydbg")
        radar2_action = Gio.MenuItem.new("Radar2", "win.radar2")
        
        reverseengineering_submenu.append_item(apktool_action)
        reverseengineering_submenu.append_item(bytecodeviewr_action)
        reverseengineering_submenu.append_item(clang_action)
        reverseengineering_submenu.append_item(clangplus_action)
        reverseengineering_submenu.append_item(cutter_action)
        reverseengineering_submenu.append_item(dex2jar_action)
        reverseengineering_submenu.append_item(edbdebugger_action)
        reverseengineering_submenu.append_item(ghidra_action)
        reverseengineering_submenu.append_item(jadxgui_action)
        reverseengineering_submenu.append_item(javasnoop_action)
        reverseengineering_submenu.append_item(jdgui_action)
        reverseengineering_submenu.append_item(NASMSHELL_action)
        reverseengineering_submenu.append_item(ollydbg_action)
        reverseengineering_submenu.append_item(radar2_action)
        
        #EXPLORATION TOOLS
        armitage_action = Gio.MenuItem.new("Armitage", "win.armitage")
        beefstart_action = Gio.MenuItem.new("Beef Start", "win.beefstart")
        crackmapper_action = Gio.MenuItem.new("Crackmapper", "win.crackmapper")
        metasploit_action = Gio.MenuItem.new("Metasploit", "win.metasploit")
        msfpayloadcreator_action = Gio.MenuItem.new("MSF Payload Creator", "win.msfpayloadcreator")
        searchsploit_action = Gio.MenuItem.new("Searchsploit", "win.searchsploit")
        shellnoob_action = Gio.MenuItem.new("Shellnoob", "win.shellnoob")
        socialengneeringtoolkit_submenu= Gio.MenuItem.new("Social Engineering Toolkit", "win.socialengneeringtoolkit")
        sqlmap_action = Gio.MenuItem.new("SQLMap", "win.sqlmap")
        terminator_action = Gio.MenuItem.new("Terminator", "win.terminator")
        
        explorationtools_submenu.append_item(armitage_action)
        explorationtools_submenu.append_item(beefstart_action)
        explorationtools_submenu.append_item(crackmapper_action)
        explorationtools_submenu.append_item(metasploit_action)
        explorationtools_submenu.append_item(msfpayloadcreator_action)
        explorationtools_submenu.append_item(searchsploit_action)
        explorationtools_submenu.append_item(shellnoob_action)
        explorationtools_submenu.append_item(socialengneeringtoolkit_submenu)
        explorationtools_submenu.append_item(sqlmap_action)
        explorationtools_submenu.append_item(terminator_action)
        
        #sniffing tools
        bettercap_action = Gio.MenuItem.new("Bettercap", "win.bettercap")
        driftnet_action = Gio.MenuItem.new("Driftnet", "win.driftnet")
        ettercap_action = Gio.MenuItem.new("Ettercap", "win.ettercap")
        fernet_action = Gio.MenuItem.new("Fernet", "win.fernet")
        hamster_action = Gio.MenuItem.new("Hamster", "win.hamster")
        macchanger_action = Gio.MenuItem.new("Macchanger", "win.macchanger")
        minicorn_action = Gio.MenuItem.new("Minicorn", "win.minicorn")
        mitmproxy_action = Gio.MenuItem.new("Mitmproxy", "win.mitmproxy")
        netsniffng_action = Gio.MenuItem.new("Netsniff-ng", "win.netsniff-ng")
        responder_action = Gio.MenuItem.new("Responder", "win.responder")
        scapy_action = Gio.MenuItem.new("Scapy", "win.scapy")
        tcpdump_action = Gio.MenuItem.new("Tcpdump", "win.tcpdump")
        wireshark_action = Gio.MenuItem.new("Wireshark", "win.wireshark")
        
        sniffingtools_submenu.append_item(bettercap_action)
        sniffingtools_submenu.append_item(driftnet_action)
        sniffingtools_submenu.append_item(ettercap_action)
        sniffingtools_submenu.append_item(fernet_action)
        sniffingtools_submenu.append_item(hamster_action)
        sniffingtools_submenu.append_item(macchanger_action)
        sniffingtools_submenu.append_item(minicorn_action)
        sniffingtools_submenu.append_item(mitmproxy_action)
        sniffingtools_submenu.append_item(netsniffng_action)
        sniffingtools_submenu.append_item(responder_action)
        sniffingtools_submenu.append_item(scapy_action)
        sniffingtools_submenu.append_item(tcpdump_action)
        sniffingtools_submenu.append_item(wireshark_action)
        
        #post exploitation tools
        backdoorfactory_acton = Gio.MenuItem.new("Backdoor Factory", "win.backdoorfactory")
        bloodhund_action = Gio.MenuItem.new("Bloodhound", "win.bloodhound")
        cymothoa_action = Gio.MenuItem.new("Cymothoa", "win.cymothoa")
        impacket_action = Gio.MenuItem.new("Impacket", "win.impacket")
        mimkatz_action = Gio.MenuItem.new("Mimkatz", "win.mimkatz")
        ncat_action = Gio.MenuItem.new("Ncat", "win.ncat")
        netcat_action = Gio.MenuItem.new("Netcat", "win.netcat")
        nishang_action = Gio.MenuItem.new("Nishang", "win.nishang")
        powershell_action = Gio.MenuItem.new("Powershell", "win.powershell")
        powersploit_action = Gio.MenuItem.new("Powersploit", "win.powersploit")
        proxychains4_action  = Gio.MenuItem.new("Proxychains4", "win.proxychain")
        shelltier_action = Gio.MenuItem.new("Shelltier", "win.shelltier")
        veil_action = Gio.MenuItem.new("Veil", "win.veil")
        weevly_action = Gio.MenuItem.new("Weevly", "win.weevly")
        
        postexploitation_submenu.append_item(backdoorfactory_acton)
        postexploitation_submenu.append_item(bloodhund_action)
        postexploitation_submenu.append_item(cymothoa_action)
        postexploitation_submenu.append_item(impacket_action)
        postexploitation_submenu.append_item(mimkatz_action)
        postexploitation_submenu.append_item(ncat_action)
        postexploitation_submenu.append_item(netcat_action)
        postexploitation_submenu.append_item(nishang_action)
        postexploitation_submenu.append_item(powershell_action)
        postexploitation_submenu.append_item(powersploit_action)
        postexploitation_submenu.append_item(proxychains4_action)
        postexploitation_submenu.append_item(shelltier_action)
        postexploitation_submenu.append_item(veil_action)
        postexploitation_submenu.append_item(weevly_action)
        
        #forensic tools
        autopsy_action = Gio.MenuItem.new("Autopsy", "win.autopsy")
        binwalk_action = Gio.MenuItem.new("Binwalk", "win.binwalk")
        bulkextractor_action = Gio.MenuItem.new("Bulk Extractor", "win.bulkextractor")
        chkrootkit_action = Gio.MenuItem.new("Chkrootkit", "win.chkrootkit")
        formost_action = Gio.MenuItem.new("Foremost", "win.foremost")
        galleta_action = Gio.MenuItem.new("Galleta", "win.galleta")
        hashdeep_action = Gio.MenuItem.new("Hashdeep", "win.hashdeep")
        rkhunter_action = Gio.MenuItem.new("Rkhunter", "win.rkhunter")
        ssdeep_action = Gio.MenuItem.new("Ssdeep", "win.ssdeep")
        unhide_action = Gio.MenuItem.new("Unhide", "win.unhide")
        yara_action = Gio.MenuItem.new("Yara", "win.yara")
        
        forensics_submenu.append_item(autopsy_action)
        forensics_submenu.append_item(binwalk_action)
        forensics_submenu.append_item(bulkextractor_action)
        forensics_submenu.append_item(chkrootkit_action)
        forensics_submenu.append_item(formost_action)
        forensics_submenu.append_item(galleta_action)
        forensics_submenu.append_item(hashdeep_action)
        forensics_submenu.append_item(rkhunter_action)
        forensics_submenu.append_item(ssdeep_action)
        forensics_submenu.append_item(unhide_action)
        forensics_submenu.append_item(yara_action)
        
        #reporting Tools
        cherrytree_action = Gio.MenuItem.new("Cherrytree", "win.cherrytree")
        cutycapt_action = Gio.MenuItem.new("Cutycapt", "win.cutycapt")
        dradis_action = Gio.MenuItem.new("Dradis", "win.dradis")
        eyewitness_action = Gio.MenuItem.new("Eyewitness", "win.eyewitness")
        faraday_action = Gio.MenuItem.new("Faraday", "win.faraday")
        meltego_action = Gio.MenuItem.new("Meltego", "win.meltego")
        pipl_action = Gio.MenuItem.new("Pipl", "win.pipl")
        recorddesktop_action = Gio.MenuItem.new("Record Desktop", "win.recorddesktop")
        
        reportingtools_submenu.append_item(cherrytree_action)
        reportingtools_submenu.append_item(cutycapt_action)
        reportingtools_submenu.append_item(dradis_action)
        reportingtools_submenu.append_item(eyewitness_action)
        reportingtools_submenu.append_item(faraday_action)
        reportingtools_submenu.append_item(meltego_action)
        reportingtools_submenu.append_item(pipl_action)
        reportingtools_submenu.append_item(recorddesktop_action)
        
        #social engineering tools
        backdoorfactory_action = Gio.MenuItem.new("Backdoor Factory", "win.backdoorfactory")
        beef_action = Gio.MenuItem.new("Beef", "win.beef")
        matelgo_action = Gio.MenuItem.new("Matelgo", "win.matelgo")
        msfpayloadcreator_action = Gio.MenuItem.new("MSF Payload Creator", "win.msfpayloadcreator")
        sherlock_action = Gio.MenuItem.new("Sherlock", "win.sherlock")
        socialengineeringtoolkit_action = Gio.MenuItem.new("Social Engineering Toolkit", "win.socialengineeringtoolkit")

        socialengineeringtoolkit_submenu.append_item(backdoorfactory_action)
        socialengineeringtoolkit_submenu.append_item(beef_action)
        socialengineeringtoolkit_submenu.append_item(matelgo_action)
        socialengineeringtoolkit_submenu.append_item(msfpayloadcreator_action)
        socialengineeringtoolkit_submenu.append_item(sherlock_action)
        socialengineeringtoolkit_submenu.append_item(socialengineeringtoolkit_action)
        
        #system services toolkit
        beefstart_action = Gio.MenuItem.new("Beefstart", "win.beefstart")
        defectdojo_action = Gio.MenuItem.new("Defect Dojo", "win.defectdojo")
        dardisstart_action = Gio.MenuItem.new("Dradis Start", "win.dradisstart")
        gvmstart_action = Gio.MenuItem.new("GVM Start", "win.gvmstart")
        xplicostart_action = Gio.MenuItem.new("Xplico Start", "win.xplicostart")
        
        systemservicestoolkit_submenu.append_item(beefstart_action)
        systemservicestoolkit_submenu.append_item(defectdojo_action)
        systemservicestoolkit_submenu.append_item(dardisstart_action)
        systemservicestoolkit_submenu.append_item(gvmstart_action)
        systemservicestoolkit_submenu.append_item(xplicostart_action)
        
        #create the submenu actions for Hardware
        hardware_menu = Gio.Menu.new()
        menu.append_submenu("Hardware Tools", hardware_menu)
        
        #Create the submenu actions for Hardware
        Hak5_action = Gio.MenuItem.new("Hak5", "win.Hak5")
        pine64_action = Gio.MenuItem.new("Pine64", "win.pine64")
        hardware_menu.append_item(Hak5_action)
        hardware_menu.append_item(pine64_action)
        #End of Hardware submenu
        
        #create the submenu actions for Training platoforms
        training_menu = Gio.Menu.new()
        menu.append_submenu("Training Platforms", training_menu)
        
        #Create the submenu actions for Training Platforms
        tryhackme_action = Gio.MenuItem.new("Tryhackme", "win.tryhackme")
        hackthebox_action = Gio.MenuItem.new("Hackthebox", "win.hackthebox")
        training_menu.append_item(tryhackme_action)
        training_menu.append_item(hackthebox_action)
        #End of Training Platforms submenu
        
        #create the submenu actions for CTF platforms
        ctf_menu = Gio.Menu.new()
        menu.append_submenu("CTF Platforms", ctf_menu)
        
        #Create the submenu actions for CTF Platforms
        picoctf_action = Gio.MenuItem.new("PicoCTF", "win.picoctf")
        ctfwithgoogle_action = Gio.MenuItem.new("CTF with Google", "win.ctfwithgoogle")
        ctf_menu.append_item(picoctf_action)
        ctf_menu.append_item(ctfwithgoogle_action)
        #End of CTF Platforms submenu
        # Create the SimpleAction objects and connect them to the functions
        self.cyberchef_action = Gio.SimpleAction.new("cyberchef", None)
        self.cyberchef_action.connect("activate", self.cyberchef)
        self.add_action(self.cyberchef_action)

        self.rot13_action = Gio.SimpleAction.new("rot13", None)
        self.rot13_action.connect("activate", self.Rot13)
        self.add_action(self.rot13_action)

        self.decode_action = Gio.SimpleAction.new("decode", None)
        self.decode_action.connect("activate", self.decode)
        self.add_action(self.decode_action)

        self.encode_action = Gio.SimpleAction.new("encode", None)
        self.encode_action.connect("activate", self.encode)
        self.add_action(self.encode_action)
        
        #Create the SimpleAction objects and connect them to the functions
        self.urlscan_action = Gio.SimpleAction.new("urlscan", None)
        self.urlscan_action.connect("activate", self.urlscan)
        self.add_action(self.urlscan_action)
        
        self.vulnhub_action = Gio.SimpleAction.new("vulnhub", None)
        self.vulnhub_action.connect("activate", self.vulnhub)
        self.add_action(self.vulnhub_action)
        
        self.opswat_action = Gio.SimpleAction.new("opswat", None)
        self.opswat_action.connect("activate", self.opswat)
        self.add_action(self.opswat_action)
        
        self.exploitdb_action = Gio.SimpleAction.new("exploitdb", None)
        self.exploitdb_action.connect("activate", self.exploitdb)
        self.add_action(self.exploitdb_action)
        #End of Web tools submenu
        
        #Create the inforamtion gathering functions
        self.amass_action = Gio.SimpleAction.new("Amass",None)
        self.amass_action.connect("activate",self.amass)
        self.add_action(self.amass_action)
       
        self.dmitry_action =Gio.SimpleAction.new("dmitry",None)
        self.dmitry_action.connect("activate",self.dmitry)
        self.add_action(self.dmitry_action)

        self.ikescan_action =Gio.SimpleAction.new("ikescan",None)
        self.ikescan_action.connect("activate",self.ikescan)
        self.add_action(self.ikescan_action)
        
        self.legionroot_action =Gio.SimpleAction.new("legionroot",None)
        self.legionroot_action.connect("activate",self.legionroot)
        self.add_action(self.legionroot_action)
        #End of the Information gathering funtions 
        
        #Create the vulnerablity analysis functions
        self.nmap_action =Gio.SimpleAction.new("nmap",None)
        self.nmap_action.connect("activate", self.nmap)
        self.add_action(self.nmap_action)
        
        self.nikto_action =Gio.SimpleAction.new("nikto",None)
        self.nikto_action.connect("activate", self.nikto)
        self.add_action(self.nikto_action)
        
        self.nexpose_action =Gio.SimpleAction.new("nexpose",None)
        self.nexpose_action.connect("activate", self.nexpose)
        self.add_action(self.nexpose_action)
        
        #End of the vulnerablity analysis functions
        
        #create the functions of webapplication analysis
        self.burpsuite_action =Gio.SimpleAction.new("burpsuite",None)
        self.burpsuite_action.connect("activate", self.burpsuite)
        self.add_action(self.burpsuite_action)
        
        self.wafw00f_action =Gio.SimpleAction.new("wafw00f",None)
        self.wafw00f_action.connect("activate", self.wafw00f)
        self.add_action(self.wafw00f_action)
        #End of the webapplication analysis functions
       
        #Create the SimpleAction objects and connect them to the functions
        self.Hak5_action = Gio.SimpleAction.new("Hak5", None)
        self.Hak5_action.connect("activate", self.Hak5)
        self.add_action(self.Hak5_action)
        
        self.pine64_action = Gio.SimpleAction.new("pine64", None)
        self.pine64_action.connect("activate", self.pine64)
        self.add_action(self.pine64_action)
        #End of Hardware submenu
        #Create the SimpleAction objects and connect them to the functions
        self.tryhackme_action = Gio.SimpleAction.new("tryhackme", None)
        self.tryhackme_action.connect("activate", self.tryhackme)
        self.add_action(self.tryhackme_action)
        
        self.hackthebox_action = Gio.SimpleAction.new("hackthebox", None)
        self.hackthebox_action.connect("activate", self.hackthebox)
        self.add_action(self.hackthebox_action)
        #End of Training Platforms submenu
        #Create the SimpleAction objects and connect them to the functions
        self.picoctf_action = Gio.SimpleAction.new("picoctf", None)
        self.picoctf_action.connect("activate", self.picoctf)
        self.add_action(self.picoctf_action)
        
        self.ctfwithgoogle_action = Gio.SimpleAction.new("ctfwithgoogle", None)
        self.ctfwithgoogle_action.connect("activate", self.ctfwithgoogle)
        self.add_action(self.ctfwithgoogle_action)
        #End of CTF Platforms submenu
        # Get the current directory of the script
        current_dir = os.path.dirname(os.path.abspath(__file__))

        # Construct the absolute file path
        css_file_path = os.path.join(current_dir, 'style.css')

        # Load CSS file
        css_provider = Gtk.CssProvider()
        css_provider.load_from_path(css_file_path)

        # Apply CSS to window
        display = Gdk.Display.get_default()
        self.add_css_class("background")
        Gtk.StyleContext.add_provider_for_display(display, css_provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

        self.popover = Gtk.PopoverMenu()
        self.popover.set_menu_model(menu)
        self.header = Gtk.HeaderBar()  # Move this line up
        self.set_titlebar(self.header)
        self.hamburger = Gtk.MenuButton()
        self.hamburger.set_popover(self.popover)
        self.hamburger.set_icon_name("open-menu-symbolic")
        self.header.pack_start(self.hamburger)  # Move this line down
        # Initialize the notification system
        Notify.init("Penetration App")
   # Define the functions for encryption submenu action
    def cyberchef(self, action, param):
        webbrowser.open_new_tab("https://cyberchef.org/")

    def Rot13(self, action, param):
        webbrowser.open_new_tab("https://rot13.com/")

    def decode(self, action, param):
        webbrowser.open_new_tab("https://www.dcode.fr/")

    def encode(self, action, param):
        webbrowser.open_new_tab("https://www.base64encode.org/")
    # End of encryption submenu action
    
    # Define the functions for web tools submenu action
    def urlscan(self, action, param):
        webbrowser.open_new_tab("https://urlscan.io/")
    def vulnhub(self, action, param):
        webbrowser.open_new_tab("https://www.vulnhub.com/")
    def opswat(self, action, param):
        webbrowser.open_new_tab("https://www.opswat.com/")
    def exploitdb(self, action, param):
        webbrowser.open_new_tab("https://www.exploit-db.com/")
    # End of web tools submenu action
    
    # Define the functions for software inforamation gathering sub-submenu action
    def amass(self,subprocess):
        print('amass')

    
    def dmitry(self,action,param):
        print('dmitry')
    
    def ikescan(self,action,parm):
        print('ikescan')
    
    def legionroot(self,action,parm):
        print('legion(root)')
        
    # Define the functions for software inforamation gathering sub-submenu action
    # Create the vulnerability analysis functions
    def nmap(self, action, parameter):
        print('nmap')

    def nikto(self, action, parameter):
        print('nikto')

    def nexpose(self, action, parameter):
        print('nexpose')
    
    # End of the vulnerablity analysis functions
    def burpsuite(self,param,parameter):
        print('brupsutie')

    def wafw00f(self,param,Parameter):
        print('wafw00f')
        
    # Define the functions for hardware submenu action
    def Hak5(self, action, param):
        webbrowser.open_new_tab("https://hak5.org/")
    def pine64(self, action, param):
        webbrowser.open_new_tab("https://pine64.com/")
    # End of hardware submenu action
    # Define the functions for training platforms submenu action
    def tryhackme(self, action, param):
        webbrowser.open_new_tab("https://tryhackme.com/")
    def hackthebox(self, action, param):
        webbrowser.open_new_tab("https://www.hackthebox.com/")
    # End of training platforms submenu action
    # Define the functions for CTF platforms submenu action
    def picoctf(self, action, param):
        webbrowser.open_new_tab("https://picoctf.org/")
    def ctfwithgoogle(self, action, param):
        webbrowser.open_new_tab("https://capturetheflag.withgoogle.com/")
    # End of CTF platforms submenu action
class MyApp(Gtk.Application):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.connect('activate',self.on_activate)
        
    def on_activate(self, app):
        self.win = MainWindow(application=app,title="Cyber City Hub")
        self.win.present()

       
if __name__ == "__main__":
    app = MyApp(application_id='org.PenetrationApp.GtkApplication')
    app.run(sys.argv)
