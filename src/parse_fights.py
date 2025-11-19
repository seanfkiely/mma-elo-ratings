import pandas as pd
import re


def _apply_manual_fixes(df: pd.DataFrame) -> pd.DataFrame:
    """
    Apply corrections for known bad rows:
    - cases where a fighter fought multiple times in one night and Wikipedia
      has one date box for these fights
    - typos in record/date columns
    - one-off cleanup for specific fighters/events
    """

    out = df.copy()

    # Enter missing date for Abdul-Kerim Edilov
    out.loc[
        (out["fighter"] == "Abdul-Kerim Edilov") & (out["record"] == "2–2"), "date"
    ] = "November 13, 2010"

    # Enter missing dates for Abubakar Nurmagomedov
    out.loc[
        (out["fighter"] == "Abubakar Nurmagomedov") & (out["record"] == "8–0"), "date"
    ] = "September 1, 2014"

    out.loc[
        (out["fighter"] == "Abubakar Nurmagomedov") & (out["record"] == "3–0"), "date"
    ] = "February 21, 2013"

    # Enter missing dates for Alan Belcher
    out.loc[(out["fighter"] == "Alan Belcher") & (out["record"] == "4–2"), "date"] = (
        "February 18, 2006"
    )

    out.loc[(out["fighter"] == "Alan Belcher") & (out["record"] == "3–2"), "date"] = (
        "February 18, 2006"
    )

    out.loc[(out["fighter"] == "Alan Belcher") & (out["record"] == "2–0"), "date"] = (
        "July 9, 2005"
    )

    # Enter missing dates for Albert Tumenov
    out.loc[(out["fighter"] == "Albert Tumenov") & (out["record"] == "4–2"), "date"] = (
        "June 8, 2012"
    )

    # Enter missing dates for Albert Tumenov
    out.loc[(out["fighter"] == "Albert Tumenov") & (out["record"] == "4–2"), "date"] = (
        "June 8, 2012"
    )

    # Enter missing dates for Aleksei Oleinik
    out.loc[
        (out["fighter"] == "Aleksei Oleinik") & (out["record"] == "40–5–1"), "date"
    ] = "November 28, 2009"

    out.loc[
        (out["fighter"] == "Aleksei Oleinik") & (out["record"] == "39–5–1"), "date"
    ] = "November 28, 2009"

    out.loc[
        (out["fighter"] == "Aleksei Oleinik") & (out["record"] == "35–5"), "date"
    ] = "October 25, 2008"

    out.loc[
        (out["fighter"] == "Aleksei Oleinik") & (out["record"] == "33–5"), "date"
    ] = "October 4, 2008"

    out.loc[
        (out["fighter"] == "Aleksei Oleinik") & (out["record"] == "32–5"), "date"
    ] = "October 4, 2008"

    out.loc[
        (out["fighter"] == "Aleksei Oleinik") & (out["record"] == "31–4"), "date"
    ] = "September 13, 2008"

    out.loc[
        (out["fighter"] == "Aleksei Oleinik") & (out["record"] == "28–3"), "date"
    ] = "April 11, 2008"

    out.loc[
        (out["fighter"] == "Aleksei Oleinik") & (out["record"] == "26–3"), "date"
    ] = "December 14, 2007"

    out.loc[
        (out["fighter"] == "Aleksei Oleinik") & (out["record"] == "25–3"), "date"
    ] = "December 14, 2007"

    out.loc[
        (out["fighter"] == "Aleksei Oleinik") & (out["record"] == "23–3"), "date"
    ] = "November 23, 2007"

    out.loc[
        (out["fighter"] == "Aleksei Oleinik") & (out["record"] == "22–3"), "date"
    ] = "November 23, 2007"

    out.loc[
        (out["fighter"] == "Aleksei Oleinik") & (out["record"] == "20–3"), "date"
    ] = "November 10, 2007"

    out.loc[
        (out["fighter"] == "Aleksei Oleinik") & (out["record"] == "19–3"), "date"
    ] = "November 10, 2007"

    out.loc[
        (out["fighter"] == "Aleksei Oleinik") & (out["record"] == "15–2"), "date"
    ] = "April 14, 2006"

    out.loc[
        (out["fighter"] == "Aleksei Oleinik") & (out["record"] == "14–2"), "date"
    ] = "April 14, 2006"

    out.loc[
        (out["fighter"] == "Aleksei Oleinik") & (out["record"] == "13–1"), "date"
    ] = "October 9, 2004"

    out.loc[
        (out["fighter"] == "Aleksei Oleinik") & (out["record"] == "11–1"), "date"
    ] = "August 27, 2004"

    out.loc[
        (out["fighter"] == "Aleksei Oleinik") & (out["record"] == "10–1"), "date"
    ] = "August 27, 2004"

    out.loc[
        (out["fighter"] == "Aleksei Oleinik") & (out["record"] == "8–1"), "date"
    ] = "December 7, 2001"

    out.loc[
        (out["fighter"] == "Aleksei Oleinik") & (out["record"] == "6–1"), "date"
    ] = "May 16, 1999"

    out.loc[
        (out["fighter"] == "Aleksei Oleinik") & (out["record"] == "2–0"), "date"
    ] = "November 10, 1996"

    out.loc[
        (out["fighter"] == "Aleksei Oleinik") & (out["record"] == "1–0"), "date"
    ] = "November 10, 1996"

    # Enter missing dates for Alexey Oleynik
    out.loc[
        (out["fighter"] == "Alexey Oleynik") & (out["record"] == "40–5–1"), "date"
    ] = "November 28, 2009"

    out.loc[
        (out["fighter"] == "Alexey Oleynik") & (out["record"] == "39–5–1"), "date"
    ] = "November 28, 2009"

    out.loc[
        (out["fighter"] == "Alexey Oleynik") & (out["record"] == "35–5"), "date"
    ] = "October 25, 2008"

    out.loc[
        (out["fighter"] == "Alexey Oleynik") & (out["record"] == "33–5"), "date"
    ] = "October 4, 2008"

    out.loc[
        (out["fighter"] == "Alexey Oleynik") & (out["record"] == "32–5"), "date"
    ] = "October 4, 2008"

    out.loc[
        (out["fighter"] == "Alexey Oleynik") & (out["record"] == "31–4"), "date"
    ] = "September 13, 2008"

    out.loc[
        (out["fighter"] == "Alexey Oleynik") & (out["record"] == "28–3"), "date"
    ] = "April 11, 2008"

    out.loc[
        (out["fighter"] == "Alexey Oleynik") & (out["record"] == "26–3"), "date"
    ] = "December 14, 2007"

    out.loc[
        (out["fighter"] == "Alexey Oleynik") & (out["record"] == "25–3"), "date"
    ] = "December 14, 2007"

    out.loc[
        (out["fighter"] == "Alexey Oleynik") & (out["record"] == "23–3"), "date"
    ] = "November 23, 2007"

    out.loc[
        (out["fighter"] == "Alexey Oleynik") & (out["record"] == "22–3"), "date"
    ] = "November 23, 2007"

    out.loc[
        (out["fighter"] == "Alexey Oleynik") & (out["record"] == "20–3"), "date"
    ] = "November 10, 2007"

    out.loc[
        (out["fighter"] == "Alexey Oleynik") & (out["record"] == "19–3"), "date"
    ] = "November 10, 2007"

    out.loc[
        (out["fighter"] == "Alexey Oleynik") & (out["record"] == "15–2"), "date"
    ] = "April 14, 2006"

    out.loc[
        (out["fighter"] == "Alexey Oleynik") & (out["record"] == "14–2"), "date"
    ] = "April 14, 2006"

    out.loc[
        (out["fighter"] == "Alexey Oleynik") & (out["record"] == "13–1"), "date"
    ] = "October 9, 2004"

    out.loc[
        (out["fighter"] == "Alexey Oleynik") & (out["record"] == "11–1"), "date"
    ] = "August 27, 2004"

    out.loc[
        (out["fighter"] == "Alexey Oleynik") & (out["record"] == "10–1"), "date"
    ] = "August 27, 2004"

    out.loc[(out["fighter"] == "Alexey Oleynik") & (out["record"] == "8–1"), "date"] = (
        "December 7, 2001"
    )

    out.loc[(out["fighter"] == "Alexey Oleynik") & (out["record"] == "6–1"), "date"] = (
        "May 16, 1999"
    )

    out.loc[(out["fighter"] == "Alexey Oleynik") & (out["record"] == "2–0"), "date"] = (
        "November 10, 1996"
    )

    out.loc[(out["fighter"] == "Alexey Oleynik") & (out["record"] == "1–0"), "date"] = (
        "November 10, 1996"
    )

    # Enter missing dates for Alistair Overeem
    out.loc[
        (out["fighter"] == "Alistair Overeem") & (out["record"] == "12–3"), "date"
    ] = "13 October 2002"

    # Enter missing dates for Amir Albazi
    out.loc[(out["fighter"] == "Amir Albazi") & (out["record"] == "1–0"), "date"] = (
        "August 22, 2009"
    )

    # Enter missing dates for Anderson Silva
    out.loc[(out["fighter"] == "Anderson Silva") & (out["record"] == "1–0"), "date"] = (
        "June 25 1997"
    )

    # Enter missing dates for Andre Winner
    out.loc[
        (out["fighter"] == "Andre Winner") & (out["record"] == "18–8–1"), "date"
    ] = "3 May 2014"

    out.loc[
        (out["fighter"] == "Andre Winner") & (out["record"] == "17–8–1"), "date"
    ] = "3 May 2014"

    # Enter missing dates for Andreas Michailidis
    out.loc[
        (out["fighter"] == "Andreas Michailidis") & (out["record"] == "3–1"), "date"
    ] = "May 29, 2011"

    # Enter missing dates for Andrei Arlovski
    out.loc[
        (out["fighter"] == "Andrei Arlovski") & (out["record"] == "1–1"), "date"
    ] = "9 April 2000"

    # Enter missing dates for André Fialho
    out.loc[(out["fighter"] == "André Fialho") & (out["record"] == "4–0"), "date"] = (
        "30 November 2014"
    )

    out.loc[(out["fighter"] == "André Fialho") & (out["record"] == "3–0"), "date"] = (
        "30 November 2014"
    )

    # Enter missing dates for Antônio Rodrigo Nogueira
    out.loc[
        (out["fighter"] == "Antônio Rodrigo Nogueira") & (out["record"] == "24–2–1"),
        "date",
    ] = "15 August 2004"

    out.loc[
        (out["fighter"] == "Antônio Rodrigo Nogueira") & (out["record"] == "10–1–1"),
        "date",
    ] = "24 February 2001"

    out.loc[
        (out["fighter"] == "Antônio Rodrigo Nogueira") & (out["record"] == "9–1–1"),
        "date",
    ] = "24 February 2001"

    out.loc[
        (out["fighter"] == "Antônio Rodrigo Nogueira") & (out["record"] == "7–1–1"),
        "date",
    ] = "9 October 2000"

    out.loc[
        (out["fighter"] == "Antônio Rodrigo Nogueira") & (out["record"] == "6–0"),
        "date",
    ] = "26 February 2000"

    out.loc[
        (out["fighter"] == "Antônio Rodrigo Nogueira") & (out["record"] == "3–0"),
        "date",
    ] = "28 October 1999"

    # Enter missing dates for Aori Qileng
    out.loc[(out["fighter"] == "Aori Qileng") & (out["record"] == "5–2"), "date"] = (
        "December 17, 2016"
    )

    # Enter missing dates for Ariane Carnelossi
    out.loc[
        (out["fighter"] == "Ariane Carnelossi") & (out["record"] == "10–1"), "date"
    ] = "November 3, 2018"

    # Enter missing dates for Azamat Bekoev
    out.loc[(out["fighter"] == "Azamat Bekoev") & (out["record"] == "5–0"), "date"] = (
        "July 30, 2017"
    )

    out.loc[(out["fighter"] == "Azamat Bekoev") & (out["record"] == "1–0"), "date"] = (
        "September 27, 2015"
    )

    # Enter missing dates for Azamat Murzakanov
    out.loc[
        (out["fighter"] == "Azamat Murzakanov") & (out["record"] == "8–0"), "date"
    ] = "November 15, 2019"

    # Enter missing dates for Ben Rothwell
    out.loc[(out["fighter"] == "Ben Rothwell") & (out["record"] == "11–1"), "date"] = (
        "April 27, 2002"
    )

    out.loc[(out["fighter"] == "Ben Rothwell") & (out["record"] == "7–1"), "date"] = (
        "February 16, 2002"
    )

    out.loc[(out["fighter"] == "Ben Rothwell") & (out["record"] == "2–0"), "date"] = (
        "April 28, 2001"
    )

    # Enter missing dates for Bobby Green
    out.loc[(out["fighter"] == "Bobby Green") & (out["record"] == "6–1"), "date"] = (
        "June 28, 2008"
    )

    out.loc[(out["fighter"] == "Bobby Green") & (out["record"] == "5–1"), "date"] = (
        "June 28, 2008"
    )

    # Enter missing dates for King Green
    out.loc[(out["fighter"] == "King Green") & (out["record"] == "6–1"), "date"] = (
        "June 28, 2008"
    )

    out.loc[(out["fighter"] == "King Green") & (out["record"] == "5–1"), "date"] = (
        "June 28, 2008"
    )

    # Enter missing dates for Bobby Hoffman
    out.loc[
        (out["fighter"] == "Bobby Hoffman") & (out["record"] == "29–5–1 (1)"), "date"
    ] = "February 21, 2003"

    out.loc[(out["fighter"] == "Bobby Hoffman") & (out["record"] == "23–3"), "date"] = (
        "December 22, 2000"
    )

    out.loc[(out["fighter"] == "Bobby Hoffman") & (out["record"] == "21–3"), "date"] = (
        "September 30, 2000"
    )

    out.loc[(out["fighter"] == "Bobby Hoffman") & (out["record"] == "18–2"), "date"] = (
        "July 15, 2000"
    )

    out.loc[(out["fighter"] == "Bobby Hoffman") & (out["record"] == "10–1"), "date"] = (
        "September 7, 1999"
    )

    out.loc[(out["fighter"] == "Bobby Hoffman") & (out["record"] == "9–1"), "date"] = (
        "September 7, 1999"
    )

    out.loc[(out["fighter"] == "Bobby Hoffman") & (out["record"] == "7–1"), "date"] = (
        "August 21, 1999"
    )

    out.loc[(out["fighter"] == "Bobby Hoffman") & (out["record"] == "4–1"), "date"] = (
        "May 15, 1999"
    )

    out.loc[(out["fighter"] == "Bobby Hoffman") & (out["record"] == "1–0"), "date"] = (
        "February 20, 1998"
    )

    # Enter missing dates for Bojan Veličković
    out.loc[
        (out["fighter"] == "Bojan Veličković") & (out["record"] == "16–7–2"), "date"
    ] = "October 20, 2018"

    out.loc[
        (out["fighter"] == "Bojan Veličković") & (out["record"] == "1–0"), "date"
    ] = "August 28, 2010"

    # Enter missing dates for Brandon Vera
    out.loc[(out["fighter"] == "Brandon Vera") & (out["record"] == "3–0"), "date"] = (
        "January 22, 2005"
    )

    # Enter missing dates for Brett Johns
    out.loc[(out["fighter"] == "Brett Johns") & (out["record"] == "8–0"), "date"] = (
        "14 September 2013"
    )

    # Enter missing dates for Brock Larson
    out.loc[(out["fighter"] == "Brock Larson") & (out["record"] == "39–8"), "date"] = (
        "October 3, 2014"
    )

    out.loc[(out["fighter"] == "Brock Larson") & (out["record"] == "38–8"), "date"] = (
        "October 3, 2014"
    )

    out.loc[(out["fighter"] == "Brock Larson") & (out["record"] == "14–0"), "date"] = (
        "July 23, 2005"
    )

    out.loc[(out["fighter"] == "Brock Larson") & (out["record"] == "13–0"), "date"] = (
        "July 23, 2005"
    )

    out.loc[(out["fighter"] == "Brock Larson") & (out["record"] == "4–0"), "date"] = (
        "March 12, 2004"
    )

    # Enter missing dates for Carlos Condit
    out.loc[(out["fighter"] == "Carlos Condit") & (out["record"] == "15–2"), "date"] = (
        "April 21, 2006"
    )

    # Enter missing dates for Chael Sonnen
    out.loc[(out["fighter"] == "Chael Sonnen") & (out["record"] == "3–0"), "date"] = (
        "April 13, 2002"
    )

    # Enter missing dates for Chan Sung Jung
    out.loc[(out["fighter"] == "Chan Sung Jung") & (out["record"] == "5–0"), "date"] = (
        "May 31, 2008"
    )

    out.loc[(out["fighter"] == "Chan Sung Jung") & (out["record"] == "4–0"), "date"] = (
        "May 31, 2008"
    )

    out.loc[(out["fighter"] == "Chan Sung Jung") & (out["record"] == "2–0"), "date"] = (
        "December 16, 2007"
    )

    # Enter missing dates for Charles Oliveira
    out.loc[
        (out["fighter"] == "Charles Oliveira") & (out["record"] == "11–0"), "date"
    ] = "February 14, 2010"

    out.loc[
        (out["fighter"] == "Charles Oliveira") & (out["record"] == "5–0"), "date"
    ] = "February 14, 2010"

    out.loc[
        (out["fighter"] == "Charles Oliveira") & (out["record"] == "2–0"), "date"
    ] = "March 15, 2008"

    out.loc[
        (out["fighter"] == "Charles Oliveira") & (out["record"] == "1–0"), "date"
    ] = "March 15, 2008"

    # Enter missing dates for Chris Brennan
    out.loc[
        (out["fighter"] == "Chris Brennan") & (out["record"] == "5–1–1"), "date"
    ] = "March 13, 1998"

    out.loc[(out["fighter"] == "Chris Brennan") & (out["record"] == "2–0"), "date"] = (
        "January 24, 1996"
    )

    # Enter missing dates for Clay Guida
    out.loc[(out["fighter"] == "Clay Guida") & (out["record"] == "11–3"), "date"] = (
        "May 20, 2005"
    )

    out.loc[(out["fighter"] == "Clay Guida") & (out["record"] == "1–2"), "date"] = (
        "April 3, 2004"
    )

    # Enter missing dates for Damian Stasiak
    out.loc[(out["fighter"] == "Damian Stasiak") & (out["record"] == "5–2"), "date"] = (
        "January 25, 2014"
    )

    out.loc[(out["fighter"] == "Damian Stasiak") & (out["record"] == "4–2"), "date"] = (
        "January 25, 2014"
    )

    out.loc[(out["fighter"] == "Damian Stasiak") & (out["record"] == "2–0"), "date"] = (
        "November 5, 2011"
    )

    out.loc[(out["fighter"] == "Damian Stasiak") & (out["record"] == "1–0"), "date"] = (
        "November 5, 2011"
    )

    # Enter missing dates for Damir Ismagulov
    out.loc[
        (out["fighter"] == "Damir Ismagulov") & (out["record"] == "13–1"), "date"
    ] = "December 15, 2016"

    out.loc[
        (out["fighter"] == "Damir Ismagulov") & (out["record"] == "12–1"), "date"
    ] = "December 15, 2016"

    # Enter missing dates for Dan Henderson
    out.loc[(out["fighter"] == "Dan Henderson") & (out["record"] == "17–4"), "date"] = (
        "September 25, 2005"
    )

    out.loc[(out["fighter"] == "Dan Henderson") & (out["record"] == "8–0"), "date"] = (
        "February 26, 2000"
    )

    out.loc[(out["fighter"] == "Dan Henderson") & (out["record"] == "7–0"), "date"] = (
        "February 26, 2000"
    )

    out.loc[(out["fighter"] == "Dan Henderson") & (out["record"] == "5–0"), "date"] = (
        "October 28, 1999"
    )

    out.loc[(out["fighter"] == "Dan Henderson") & (out["record"] == "3–0"), "date"] = (
        "May 15, 1998"
    )

    out.loc[(out["fighter"] == "Dan Henderson") & (out["record"] == "1–0"), "date"] = (
        "June 15, 1997"
    )

    # Enter missing dates for Dan Severn
    out.loc[(out["fighter"] == "Dan Severn") & (out["record"] == "7–2"), "date"] = (
        "December 16, 1995"
    )

    out.loc[(out["fighter"] == "Dan Severn") & (out["record"] == "6–2"), "date"] = (
        "December 16, 1995"
    )

    out.loc[(out["fighter"] == "Dan Severn") & (out["record"] == "4–1"), "date"] = (
        "April 7, 1995"
    )

    out.loc[(out["fighter"] == "Dan Severn") & (out["record"] == "3–1"), "date"] = (
        "April 7, 1995"
    )

    out.loc[(out["fighter"] == "Dan Severn") & (out["record"] == "2–0"), "date"] = (
        "December 16, 1994"
    )

    out.loc[(out["fighter"] == "Dan Severn") & (out["record"] == "1–0"), "date"] = (
        "December 16, 1994"
    )

    # Enter missing dates for Daniel Omielańczuk
    out.loc[
        (out["fighter"] == "Daniel Omielańczuk") & (out["record"] == "13–3–1 (1)"),
        "date",
    ] = "November 9, 2012"

    out.loc[
        (out["fighter"] == "Daniel Omielańczuk") & (out["record"] == "10–3–1 (1)"),
        "date",
    ] = "May 25, 2012"

    out.loc[
        (out["fighter"] == "Daniel Omielańczuk") & (out["record"] == "1–1"), "date"
    ] = "December 11, 2009"

    # Enter missing dates for Dave Beneteau
    out.loc[(out["fighter"] == "Dave Beneteau") & (out["record"] == "3–3"), "date"] = (
        "October 22, 1996"
    )

    out.loc[(out["fighter"] == "Dave Beneteau") & (out["record"] == "2–0"), "date"] = (
        "April 7, 1995"
    )

    out.loc[(out["fighter"] == "Dave Beneteau") & (out["record"] == "1–0"), "date"] = (
        "April 7, 1995"
    )

    # Enter missing dates for David Michaud
    out.loc[(out["fighter"] == "David Michaud") & (out["record"] == "17–5"), "date"] = (
        "October 11, 2019"
    )

    # Enter missing dates for Demian Maia
    out.loc[(out["fighter"] == "Demian Maia") & (out["record"] == "4–0"), "date"] = (
        "7 October 2006"
    )

    out.loc[(out["fighter"] == "Demian Maia") & (out["record"] == "3–0"), "date"] = (
        "7 October 2006"
    )

    # Enter missing dates for Denis Kang
    out.loc[(out["fighter"] == "Denis Kang") & (out["record"] == "3–0"), "date"] = (
        "April 24, 1999"
    )

    # Enter missing dates for Dennis Hallman
    out.loc[
        (out["fighter"] == "Dennis Hallman") & (out["record"] == "10–0"), "date"
    ] = "October 17, 1998"

    out.loc[(out["fighter"] == "Dennis Hallman") & (out["record"] == "9–0"), "date"] = (
        "October 17, 1998"
    )

    out.loc[(out["fighter"] == "Dennis Hallman") & (out["record"] == "1–0"), "date"] = (
        "May 18, 1996"
    )

    # Enter missing dates for Diego Brandao
    out.loc[(out["fighter"] == "Diego Brandao") & (out["record"] == "5–2"), "date"] = (
        "29 September 2007"
    )

    # Enter missing dates for Diego Brandão
    out.loc[(out["fighter"] == "Diego Brandão") & (out["record"] == "5–2"), "date"] = (
        "29 September 2007"
    )

    # Enter missing dates for Don Frye
    out.loc[(out["fighter"] == "Don Frye") & (out["record"] == "9–1"), "date"] = (
        "December 7, 1996"
    )

    out.loc[(out["fighter"] == "Don Frye") & (out["record"] == "8–1"), "date"] = (
        "December 7, 1996"
    )

    out.loc[(out["fighter"] == "Don Frye") & (out["record"] == "6–0"), "date"] = (
        "July 12, 1996"
    )

    out.loc[(out["fighter"] == "Don Frye") & (out["record"] == "5–0"), "date"] = (
        "July 12, 1996"
    )

    out.loc[(out["fighter"] == "Don Frye") & (out["record"] == "2–0"), "date"] = (
        "February 16, 1996"
    )

    out.loc[(out["fighter"] == "Don Frye") & (out["record"] == "1–0"), "date"] = (
        "February 16, 1996"
    )

    # Enter missing dates for Edwin Dewees
    out.loc[
        (out["fighter"] == "Edwin Dewees") & (out["record"] == "38–17 (1)"), "date"
    ] = "December 15, 2012"

    out.loc[
        (out["fighter"] == "Edwin Dewees") & (out["record"] == "38–16 (1)"), "date"
    ] = "October 20, 2012"

    out.loc[(out["fighter"] == "Edwin Dewees") & (out["record"] == "10–3"), "date"] = (
        "November 19, 2000"
    )

    out.loc[(out["fighter"] == "Edwin Dewees") & (out["record"] == "7–3"), "date"] = (
        "October 4, 2000"
    )

    out.loc[(out["fighter"] == "Edwin Dewees") & (out["record"] == "6–3"), "date"] = (
        "October 4, 2000"
    )

    out.loc[(out["fighter"] == "Edwin Dewees") & (out["record"] == "4–3"), "date"] = (
        "September 24, 2000"
    )

    # Enter missing dates for Elizeu Zaleski dos Santos
    out.loc[
        (out["fighter"] == "Elizeu Zaleski dos Santos") & (out["record"] == "10–3"),
        "date",
    ] = "May 3, 2013"

    out.loc[
        (out["fighter"] == "Elizeu Zaleski dos Santos") & (out["record"] == "9–3"),
        "date",
    ] = "May 3, 2013"

    # Enter missing dates for Evan Tanner
    out.loc[(out["fighter"] == "Evan Tanner") & (out["record"] == "11–1"), "date"] = (
        "July 7, 1998"
    )

    out.loc[(out["fighter"] == "Evan Tanner") & (out["record"] == "8–1"), "date"] = (
        "April 18, 1998"
    )

    out.loc[(out["fighter"] == "Evan Tanner") & (out["record"] == "6–0"), "date"] = (
        "November 22, 1997"
    )

    out.loc[(out["fighter"] == "Evan Tanner") & (out["record"] == "5–0"), "date"] = (
        "November 22, 1997"
    )

    out.loc[(out["fighter"] == "Evan Tanner") & (out["record"] == "2–0"), "date"] = (
        "April 12, 1997"
    )

    out.loc[(out["fighter"] == "Evan Tanner") & (out["record"] == "1–0"), "date"] = (
        "April 12, 1997"
    )

    # Enter missing dates for Fabiano Iha
    out.loc[(out["fighter"] == "Fabiano Iha") & (out["record"] == "2–0"), "date"] = (
        "November 21, 1998"
    )

    # Enter missing dates for Francis Carmont
    out.loc[
        (out["fighter"] == "Francis Carmont") & (out["record"] == "24–10"), "date"
    ] = "September 19, 2015"

    # Enter missing dates for Francis Ngannou
    out.loc[
        (out["fighter"] == "Francis Ngannou") & (out["record"] == "2–1"), "date"
    ] = "5 April 2014"

    # Enter missing dates for Frank Shamrock
    out.loc[(out["fighter"] == "Frank Shamrock") & (out["record"] == "1–0"), "date"] = (
        "December 16, 1994"
    )

    # Enter missing dates for Fábio Gurgel
    out.loc[(out["fighter"] == "Fábio Gurgel") & (out["record"] == "3–1"), "date"] = (
        "January 19, 1997"
    )

    out.loc[(out["fighter"] == "Fábio Gurgel") & (out["record"] == "2–1"), "date"] = (
        "January 19, 1997"
    )

    # Enter missing dates for Gary Goodridge
    out.loc[(out["fighter"] == "Gary Goodridge") & (out["record"] == "5–5"), "date"] = (
        "July 6, 1997"
    )

    out.loc[(out["fighter"] == "Gary Goodridge") & (out["record"] == "4–5"), "date"] = (
        "July 6, 1997"
    )

    out.loc[(out["fighter"] == "Gary Goodridge") & (out["record"] == "3–2"), "date"] = (
        "July 12, 1996"
    )

    out.loc[(out["fighter"] == "Gary Goodridge") & (out["record"] == "2–0"), "date"] = (
        "February 16, 1996"
    )

    out.loc[(out["fighter"] == "Gary Goodridge") & (out["record"] == "1–0"), "date"] = (
        "February 16, 1996"
    )

    # Enter missing dates for Gegard Mousasi
    out.loc[
        (out["fighter"] == "Gegard Mousasi") & (out["record"] == "23–2–1"), "date"
    ] = "23 September 2008"

    # Enter missing dates for Gerard Gordeau
    out.loc[(out["fighter"] == "Gerard Gordeau") & (out["record"] == "2–0"), "date"] = (
        "12 November 1993"
    )

    out.loc[(out["fighter"] == "Gerard Gordeau") & (out["record"] == "1–0"), "date"] = (
        "12 November 1993"
    )

    # Enter missing dates for Gilbert Yvel
    out.loc[(out["fighter"] == "Gilbert Yvel") & (out["record"] == "18–3"), "date"] = (
        "22 December 1999"
    )

    out.loc[(out["fighter"] == "Gilbert Yvel") & (out["record"] == "9–0"), "date"] = (
        "12 April 1998"
    )

    out.loc[(out["fighter"] == "Gilbert Yvel") & (out["record"] == "5–0"), "date"] = (
        "1 November 1997"
    )

    # Enter missing dates for Grant Dawson
    out.loc[(out["fighter"] == "Grant Dawson") & (out["record"] == "6–0"), "date"] = (
        "August 15, 2015"
    )

    # Enter missing dates for Guy Mezger
    out.loc[
        (out["fighter"] == "Guy Mezger") & (out["record"] == "12–4–2 (1)"), "date"
    ] = "May 30, 1997"

    out.loc[
        (out["fighter"] == "Guy Mezger") & (out["record"] == "5–2–1 (1)"), "date"
    ] = "April 7, 1996"

    # Enter missing dates for Heath Herring
    out.loc[(out["fighter"] == "Heath Herring") & (out["record"] == "11–4"), "date"] = (
        "September 27, 1999"
    )

    out.loc[(out["fighter"] == "Heath Herring") & (out["record"] == "10–4"), "date"] = (
        "September 27, 1999"
    )

    out.loc[(out["fighter"] == "Heath Herring") & (out["record"] == "9–3"), "date"] = (
        "September 7, 1999"
    )

    out.loc[(out["fighter"] == "Heath Herring") & (out["record"] == "8–2"), "date"] = (
        "July 1, 1999"
    )

    out.loc[(out["fighter"] == "Heath Herring") & (out["record"] == "7–2"), "date"] = (
        "July 1, 1999"
    )

    out.loc[(out["fighter"] == "Heath Herring") & (out["record"] == "5–2"), "date"] = (
        "June 1, 1999"
    )

    out.loc[(out["fighter"] == "Heath Herring") & (out["record"] == "3–1"), "date"] = (
        "April 17, 1999"
    )

    # Enter missing dates for Humberto Bandenay
    out.loc[
        (out["fighter"] == "Humberto Bandenay") & (out["record"] == "17–7 (1)"), "date"
    ] = "December 20, 2019"

    out.loc[
        (out["fighter"] == "Humberto Bandenay") & (out["record"] == "16–7 (1)"), "date"
    ] = "December 20, 2019"

    # Enter missing dates for Ikuhisa Minowa
    out.loc[
        (out["fighter"] == "Ikuhisa Minowa") & (out["record"] == "30–21–8"), "date"
    ] = "September 25, 2005"

    out.loc[
        (out["fighter"] == "Ikuhisa Minowa") & (out["record"] == "16–11–6"), "date"
    ] = "September 24, 2000"

    out.loc[
        (out["fighter"] == "Ikuhisa Minowa") & (out["record"] == "14–11–6"), "date"
    ] = "July 23, 2000"

    out.loc[
        (out["fighter"] == "Ikuhisa Minowa") & (out["record"] == "9–10–5"), "date"
    ] = "August 1, 1999"

    out.loc[
        (out["fighter"] == "Ikuhisa Minowa") & (out["record"] == "8–10–5"), "date"
    ] = "August 1, 1999"

    # Enter missing dates for Irene Aldana
    out.loc[(out["fighter"] == "Irene Aldana") & (out["record"] == "2–0"), "date"] = (
        "October 12, 2013"
    )

    # Enter missing dates for Jan Błachowicz
    out.loc[(out["fighter"] == "Jan Błachowicz") & (out["record"] == "9–2"), "date"] = (
        "May 7, 2010"
    )

    out.loc[(out["fighter"] == "Jan Błachowicz") & (out["record"] == "5–2"), "date"] = (
        "May 9, 2008"
    )

    out.loc[(out["fighter"] == "Jan Błachowicz") & (out["record"] == "4–2"), "date"] = (
        "May 9, 2008"
    )

    out.loc[(out["fighter"] == "Jan Błachowicz") & (out["record"] == "2–1"), "date"] = (
        "September 15, 2007"
    )

    out.loc[(out["fighter"] == "Jan Błachowicz") & (out["record"] == "1–1"), "date"] = (
        "September 15, 2007"
    )

    # Enter missing dates for Jared Rosholt
    out.loc[(out["fighter"] == "Jared Rosholt") & (out["record"] == "19–7"), "date"] = (
        "October 31, 2019"
    )

    out.loc[(out["fighter"] == "Jared Rosholt") & (out["record"] == "17–6"), "date"] = (
        "October 5, 2018"
    )

    out.loc[(out["fighter"] == "Jared Rosholt") & (out["record"] == "17–5"), "date"] = (
        "October 5, 2018"
    )

    # Enter missing dates for Jeremy Kennedy
    out.loc[
        (out["fighter"] == "Jeremy Kennedy") & (out["record"] == "15–2"), "date"
    ] = "October 17, 2019"

    # Enter missing dates for Jerry Bohlander
    out.loc[
        (out["fighter"] == "Jerry Bohlander") & (out["record"] == "6–1"), "date"
    ] = "February 7, 1997"

    out.loc[
        (out["fighter"] == "Jerry Bohlander") & (out["record"] == "3–1"), "date"
    ] = "June 28, 1996"

    out.loc[
        (out["fighter"] == "Jerry Bohlander") & (out["record"] == "2–0"), "date"
    ] = "February 16, 1996"

    # Enter missing dates for Jiří Procházka
    out.loc[
        (out["fighter"] == "Jiří Procházka") & (out["record"] == "16–2–1"), "date"
    ] = "December 31, 2015"

    # Enter missing dates for Joe Lauzon
    out.loc[(out["fighter"] == "Joe Lauzon") & (out["record"] == "12–3"), "date"] = (
        "April 1, 2006"
    )

    out.loc[(out["fighter"] == "Joe Lauzon") & (out["record"] == "11–3"), "date"] = (
        "April 1, 2006"
    )

    # Enter missing dates for Joe Stevenson
    out.loc[(out["fighter"] == "Joe Stevenson") & (out["record"] == "2–0"), "date"] = (
        "June 1, 1999"
    )

    # Enter missing dates for John Castañeda
    out.loc[
        (out["fighter"] == "John Castañeda") & (out["record"] == "16–2"), "date"
    ] = "November 11, 2017"

    out.loc[
        (out["fighter"] == "John Castañeda") & (out["record"] == "15–2"), "date"
    ] = "November 11, 2017"

    # Enter missing dates for John Lineker
    out.loc[(out["fighter"] == "John Lineker") & (out["record"] == "13–5"), "date"] = (
        "February 19, 2011"
    )

    out.loc[(out["fighter"] == "John Lineker") & (out["record"] == "7–5"), "date"] = (
        "February 5, 2010"
    )

    # Enter missing dates for John Teixeira
    out.loc[(out["fighter"] == "John Teixeira") & (out["record"] == "2–0"), "date"] = (
        "September 15, 2007"
    )

    # Enter missing dates for Johnny Eduardo
    out.loc[
        (out["fighter"] == "Johnny Eduardo") & (out["record"] == "11–1"), "date"
    ] = "August 23, 1998"

    out.loc[
        (out["fighter"] == "Johnny Eduardo") & (out["record"] == "10–1"), "date"
    ] = "August 23, 1998"

    out.loc[(out["fighter"] == "Johnny Eduardo") & (out["record"] == "4–1"), "date"] = (
        "August 30, 1997"
    )

    out.loc[(out["fighter"] == "Johnny Eduardo") & (out["record"] == "2–1"), "date"] = (
        "April 5, 1997"
    )

    # Enter missing dates for Jon Fitch
    out.loc[(out["fighter"] == "Jon Fitch") & (out["record"] == "9–2 (1)"), "date"] = (
        "December 17, 2004"
    )

    out.loc[(out["fighter"] == "Jon Fitch") & (out["record"] == "8–2 (1)"), "date"] = (
        "December 17, 2004"
    )

    out.loc[(out["fighter"] == "Jon Fitch") & (out["record"] == "2–1"), "date"] = (
        "September 7, 2002"
    )

    # Enter missing dates for Jorge Patino
    out.loc[
        (out["fighter"] == "Jorge Patino") & (out["record"] == "38–16–2 (1)"), "date"
    ] = "November 20, 2015"

    # Enter missing dates for Juliana Lima
    out.loc[(out["fighter"] == "Juliana Lima") & (out["record"] == "10–5"), "date"] = (
        "May 3, 2019"
    )

    # Enter missing dates for Jung Chan-sung
    out.loc[(out["fighter"] == "Jung Chan-sung") & (out["record"] == "5–0"), "date"] = (
        "May 31, 2008"
    )

    out.loc[(out["fighter"] == "Jung Chan-sung") & (out["record"] == "4–0"), "date"] = (
        "May 31, 2008"
    )

    out.loc[(out["fighter"] == "Jung Chan-sung") & (out["record"] == "2–0"), "date"] = (
        "December 16, 2007"
    )

    # Enter missing dates for Kai Asakura
    out.loc[(out["fighter"] == "Kai Asakura") & (out["record"] == "19–3"), "date"] = (
        "December 31, 2021"
    )

    # Enter missing dates for Kailin Curran
    out.loc[(out["fighter"] == "Kailin Curran") & (out["record"] == "6–6"), "date"] = (
        "May 3, 2019"
    )

    out.loc[(out["fighter"] == "Kailin Curran") & (out["record"] == "5–6"), "date"] = (
        "May 3, 2019"
    )

    # Enter missing dates for Kang Kyung-ho
    out.loc[(out["fighter"] == "Kang Kyung-ho") & (out["record"] == "10–6"), "date"] = (
        "June 16, 2012"
    )

    # Enter missing dates for Kazushi Sakuraba
    out.loc[
        (out["fighter"] == "Kazushi Sakuraba") & (out["record"] == "9–1–1 (1)"), "date"
    ] = "May 1, 2000"

    out.loc[
        (out["fighter"] == "Kazushi Sakuraba") & (out["record"] == "0–1 (1)"), "date"
    ] = "December 21, 1997"

    # Enter missing dates for Keiichiro Yamamiya
    out.loc[
        (out["fighter"] == "Keiichiro Yamamiya") & (out["record"] == "21–13–5"), "date"
    ] = "September 24, 2000"

    out.loc[
        (out["fighter"] == "Keiichiro Yamamiya") & (out["record"] == "7–7–1"), "date"
    ] = "July 21, 1997"

    out.loc[
        (out["fighter"] == "Keiichiro Yamamiya") & (out["record"] == "1–2"), "date"
    ] = "September 7, 1996"

    # Enter missing dates for Keith Hackney
    out.loc[(out["fighter"] == "Keith Hackney") & (out["record"] == "2–0"), "date"] = (
        "December 16, 1994"
    )

    # Enter missing dates for Kelly Dullanty
    out.loc[(out["fighter"] == "Kelly Dullanty") & (out["record"] == "3–0"), "date"] = (
        "June 15, 2001"
    )

    # Enter missing dates for Ken Shamrock
    out.loc[(out["fighter"] == "Ken Shamrock") & (out["record"] == "14–3"), "date"] = (
        "December 17, 1994"
    )

    out.loc[(out["fighter"] == "Ken Shamrock") & (out["record"] == "12–3"), "date"] = (
        "December 16, 1994"
    )

    out.loc[(out["fighter"] == "Ken Shamrock") & (out["record"] == "9–3"), "date"] = (
        "September 9, 1994"
    )

    out.loc[(out["fighter"] == "Ken Shamrock") & (out["record"] == "4–0"), "date"] = (
        "November 12, 1993"
    )

    # Enter missing dates for Kevin Jackson
    out.loc[(out["fighter"] == "Kevin Jackson") & (out["record"] == "2–0"), "date"] = (
        "July 27, 1997"
    )

    # Enter missing dates for Kevin Randleman
    out.loc[
        (out["fighter"] == "Kevin Randleman") & (out["record"] == "6–1"), "date"
    ] = "June 15, 1997"

    out.loc[
        (out["fighter"] == "Kevin Randleman") & (out["record"] == "5–0"), "date"
    ] = "March 3, 1997"

    out.loc[
        (out["fighter"] == "Kevin Randleman") & (out["record"] == "4–0"), "date"
    ] = "March 3, 1997"

    out.loc[
        (out["fighter"] == "Kevin Randleman") & (out["record"] == "2–0"), "date"
    ] = "October 22, 1996"

    out.loc[
        (out["fighter"] == "Kevin Randleman") & (out["record"] == "1–0"), "date"
    ] = "October 22, 1996"

    # Enter missing dates for Kevin Rosier
    out.loc[(out["fighter"] == "Kevin Rosier") & (out["record"] == "1–0"), "date"] = (
        "November 12, 1993"
    )

    # Enter missing dates for Khabib Nurmagomedov
    out.loc[
        (out["fighter"] == "Khabib Nurmagomedov") & (out["record"] == "5–0"), "date"
    ] = "8 August 2009"

    out.loc[
        (out["fighter"] == "Khabib Nurmagomedov") & (out["record"] == "3–0"), "date"
    ] = "11 October 2008"

    out.loc[
        (out["fighter"] == "Khabib Nurmagomedov") & (out["record"] == "2–0"), "date"
    ] = "11 October 2008"

    # Enter missing dates for Khadis Ibragimov
    out.loc[
        (out["fighter"] == "Khadis Ibragimov") & (out["record"] == "2–0"), "date"
    ] = "June 12, 2017"

    # Enter missing dates for Kyoji Horiguchi
    out.loc[
        (out["fighter"] == "Kyoji Horiguchi") & (out["record"] == "22–2"), "date"
    ] = "December 31, 2017"

    # Enter missing dates for Lee Murray
    out.loc[(out["fighter"] == "Lee Murray") & (out["record"] == "3–0"), "date"] = (
        "17 June 2000"
    )

    # Enter missing dates for Magomed Bibulatov
    out.loc[
        (out["fighter"] == "Magomed Bibulatov") & (out["record"] == "3–0"), "date"
    ] = "August 24, 2013"

    out.loc[
        (out["fighter"] == "Magomed Bibulatov") & (out["record"] == "2–0"), "date"
    ] = "August 24, 2013"

    # Enter missing dates for Magomed Mustafaev
    out.loc[
        (out["fighter"] == "Magomed Mustafaev") & (out["record"] == "10–1"), "date"
    ] = "September 1, 2014"

    out.loc[
        (out["fighter"] == "Magomed Mustafaev") & (out["record"] == "5–1"), "date"
    ] = "September 15, 2013"

    out.loc[
        (out["fighter"] == "Magomed Mustafaev") & (out["record"] == "3–1"), "date"
    ] = "January 16, 2013"

    # Enter missing dates for Marcin Held
    out.loc[(out["fighter"] == "Marcin Held") & (out["record"] == "6–0"), "date"] = (
        "December 6, 2009"
    )

    out.loc[(out["fighter"] == "Marcin Held") & (out["record"] == "5–0"), "date"] = (
        "December 6, 2009"
    )

    # Enter missing dates for Marcin Tybura
    out.loc[(out["fighter"] == "Marcin Tybura") & (out["record"] == "1–0"), "date"] = (
        "November 5, 2011"
    )

    # Enter missing dates for Marco Ruas
    out.loc[(out["fighter"] == "Marco Ruas") & (out["record"] == "5–0–1"), "date"] = (
        "16 December 1995"
    )

    out.loc[(out["fighter"] == "Marco Ruas") & (out["record"] == "3–0–1"), "date"] = (
        "8 September 1995"
    )

    out.loc[(out["fighter"] == "Marco Ruas") & (out["record"] == "2–0–1"), "date"] = (
        "8 September 1995"
    )

    # Enter missing dates for Mark Coleman
    out.loc[(out["fighter"] == "Mark Coleman") & (out["record"] == "10–4"), "date"] = (
        "May 1, 2000"
    )

    out.loc[(out["fighter"] == "Mark Coleman") & (out["record"] == "9–4"), "date"] = (
        "May 1, 2000"
    )

    out.loc[(out["fighter"] == "Mark Coleman") & (out["record"] == "4–0"), "date"] = (
        "September 20, 1996"
    )

    out.loc[(out["fighter"] == "Mark Coleman") & (out["record"] == "2–0"), "date"] = (
        "July 12, 1996"
    )

    out.loc[(out["fighter"] == "Mark Coleman") & (out["record"] == "1–0"), "date"] = (
        "July 12, 1996"
    )

    # Enter missing dates for Masanori Kanehara
    out.loc[
        (out["fighter"] == "Masanori Kanehara") & (out["record"] == "13–5–5"), "date"
    ] = "August 2, 2009"

    # Enter missing dates for Maurício Rua
    out.loc[(out["fighter"] == "Maurício Rua") & (out["record"] == "11–1"), "date"] = (
        "28 August 2005"
    )

    out.loc[(out["fighter"] == "Maurício Rua") & (out["record"] == "4–0"), "date"] = (
        "6 September 2003"
    )

    # Enter missing dates for Maurício Ruffy
    out.loc[(out["fighter"] == "Maurício Ruffy") & (out["record"] == "7–1"), "date"] = (
        "May 26, 2023"
    )

    # Enter missing dates for Maxim Grishin
    out.loc[(out["fighter"] == "Maxim Grishin") & (out["record"] == "1–0"), "date"] = (
        "May 24, 2008"
    )

    # Enter missing dates for Michihiro Omigawa
    out.loc[
        (out["fighter"] == "Michihiro Omigawa") & (out["record"] == "7–7–1"), "date"
    ] = "August 2, 2009"

    # Enter missing dates for Mickael Lebout
    out.loc[(out["fighter"] == "Mickael Lebout") & (out["record"] == "4–0"), "date"] = (
        "December 10, 2011"
    )

    out.loc[(out["fighter"] == "Mickael Lebout") & (out["record"] == "3–0"), "date"] = (
        "December 10, 2011"
    )

    # Enter missing dates for Mickaël Lebout
    out.loc[(out["fighter"] == "Mickaël Lebout") & (out["record"] == "4–0"), "date"] = (
        "December 10, 2011"
    )

    out.loc[(out["fighter"] == "Mickaël Lebout") & (out["record"] == "3–0"), "date"] = (
        "December 10, 2011"
    )

    # Enter missing dates for Miesha Tate
    out.loc[(out["fighter"] == "Miesha Tate") & (out["record"] == "10–2"), "date"] = (
        "August 13, 2010"
    )

    out.loc[(out["fighter"] == "Miesha Tate") & (out["record"] == "1–0"), "date"] = (
        "November 24, 2007"
    )

    # Enter missing dates for Mike Van Arsdale
    out.loc[
        (out["fighter"] == "Mike Van Arsdale") & (out["record"] == "2–0"), "date"
    ] = "February 7, 1998"

    out.loc[
        (out["fighter"] == "Mike Van Arsdale") & (out["record"] == "1–0"), "date"
    ] = "February 7, 1998"

    # Enter missing dates for Mike van Arsdale
    out.loc[
        (out["fighter"] == "Mike van Arsdale") & (out["record"] == "2–0"), "date"
    ] = "February 7, 1998"

    out.loc[
        (out["fighter"] == "Mike van Arsdale") & (out["record"] == "1–0"), "date"
    ] = "February 7, 1998"

    # Enter missing dates for Mirko Cro Cop
    out.loc[
        (out["fighter"] == "Mirko Cro Cop") & (out["record"] == "34–11–2 (1)"), "date"
    ] = "December 31, 2016"

    out.loc[
        (out["fighter"] == "Mirko Cro Cop") & (out["record"] == "20–4–2"), "date"
    ] = "September 10, 2006"

    # Enter missing dates for Nick Diaz
    out.loc[(out["fighter"] == "Nick Diaz") & (out["record"] == "4–0"), "date"] = (
        "September 28, 2002"
    )

    out.loc[(out["fighter"] == "Nick Diaz") & (out["record"] == "3–0"), "date"] = (
        "September 28, 2002"
    )

    # Enter missing dates for Norifumi Yamamoto
    out.loc[
        (out["fighter"] == "Norifumi Yamamoto") & (out["record"] == "11–1 (1)"), "date"
    ] = "September 7, 2005"

    # Enter missing dates for Nursulton Ruziboev
    out.loc[
        (out["fighter"] == "Nursulton Ruziboev") & (out["record"] == "12–3"), "date"
    ] = "May 20, 2017"

    out.loc[
        (out["fighter"] == "Nursulton Ruziboev") & (out["record"] == "11–3"), "date"
    ] = "May 20, 2017"

    # Enter missing dates for Oleg Taktarov
    out.loc[
        (out["fighter"] == "Oleg Taktarov") & (out["record"] == "13–5–2"), "date"
    ] = "February 21, 1998"

    out.loc[
        (out["fighter"] == "Oleg Taktarov") & (out["record"] == "9–1–1"), "date"
    ] = "December 16, 1995"

    out.loc[
        (out["fighter"] == "Oleg Taktarov") & (out["record"] == "8–1–1"), "date"
    ] = "December 16, 1995"

    out.loc[(out["fighter"] == "Oleg Taktarov") & (out["record"] == "6–1"), "date"] = (
        "July 14, 1995"
    )

    out.loc[(out["fighter"] == "Oleg Taktarov") & (out["record"] == "5–1"), "date"] = (
        "July 14, 1995"
    )

    out.loc[(out["fighter"] == "Oleg Taktarov") & (out["record"] == "4–0"), "date"] = (
        "April 7, 1995"
    )

    out.loc[(out["fighter"] == "Oleg Taktarov") & (out["record"] == "1–0"), "date"] = (
        "October 22, 1993"
    )

    # Enter missing dates for Omari Akhmedov
    out.loc[(out["fighter"] == "Omari Akhmedov") & (out["record"] == "7–1"), "date"] = (
        "April 12, 2012"
    )

    out.loc[(out["fighter"] == "Omari Akhmedov") & (out["record"] == "6–1"), "date"] = (
        "April 12, 2012"
    )

    out.loc[(out["fighter"] == "Omari Akhmedov") & (out["record"] == "4–1"), "date"] = (
        "October 1, 2011"
    )

    # Enter missing dates for Orlando Wiet
    out.loc[(out["fighter"] == "Orlando Wiet") & (out["record"] == "1–0"), "date"] = (
        "March 11, 1994"
    )

    # Enter missing dates for Pat Miletich
    out.loc[
        (out["fighter"] == "Pat Miletich") & (out["record"] == "18–1–1"), "date"
    ] = "March 13, 1998"

    out.loc[(out["fighter"] == "Pat Miletich") & (out["record"] == "7–0"), "date"] = (
        "February 10, 1996"
    )

    out.loc[(out["fighter"] == "Pat Miletich") & (out["record"] == "6–0"), "date"] = (
        "February 10, 1996"
    )

    out.loc[(out["fighter"] == "Pat Miletich") & (out["record"] == "4–0"), "date"] = (
        "January 20, 1996"
    )

    out.loc[(out["fighter"] == "Pat Miletich") & (out["record"] == "2–0"), "date"] = (
        "October 28, 1995"
    )

    out.loc[(out["fighter"] == "Pat Miletich") & (out["record"] == "1–0"), "date"] = (
        "October 28, 1995"
    )

    # Enter missing dates for Paul Varelans
    out.loc[(out["fighter"] == "Paul Varelans") & (out["record"] == "8–8"), "date"] = (
        "February 3, 1998"
    )

    out.loc[(out["fighter"] == "Paul Varelans") & (out["record"] == "5–3"), "date"] = (
        "March 30, 1996"
    )

    out.loc[(out["fighter"] == "Paul Varelans") & (out["record"] == "3–1"), "date"] = (
        "September 8, 1995"
    )

    out.loc[(out["fighter"] == "Paul Varelans") & (out["record"] == "2–1"), "date"] = (
        "September 8, 1995"
    )

    out.loc[(out["fighter"] == "Paul Varelans") & (out["record"] == "1–0"), "date"] = (
        "July 14, 1995"
    )

    # Enter missing dates for Paulo Thiago
    out.loc[(out["fighter"] == "Paulo Thiago") & (out["record"] == "3–0"), "date"] = (
        "October 13, 2006"
    )

    out.loc[(out["fighter"] == "Paulo Thiago") & (out["record"] == "2–0"), "date"] = (
        "October 13, 2006"
    )

    # Enter missing dates for Philipe Lins
    out.loc[(out["fighter"] == "Philipe Lins") & (out["record"] == "12–3"), "date"] = (
        "October 5, 2018"
    )

    # Enter missing dates for Quinton Jackson
    out.loc[
        (out["fighter"] == "Quinton Jackson") & (out["record"] == "19–3"), "date"
    ] = "November 9, 2003"

    # Enter missing dates for Rafael dos Anjos
    out.loc[
        (out["fighter"] == "Rafael dos Anjos") & (out["record"] == "6–2"), "date"
    ] = "29 April 2007"

    # Enter missing dates for Ramazan Emeev
    out.loc[(out["fighter"] == "Ramazan Emeev") & (out["record"] == "1–0"), "date"] = (
        "October 24, 2009"
    )

    # Enter missing dates for Randy Couture
    out.loc[(out["fighter"] == "Randy Couture") & (out["record"] == "8–2"), "date"] = (
        "February 24, 2001"
    )

    out.loc[(out["fighter"] == "Randy Couture") & (out["record"] == "5–2"), "date"] = (
        "October 9, 2000"
    )

    out.loc[(out["fighter"] == "Randy Couture") & (out["record"] == "1–0"), "date"] = (
        "May 30, 1997"
    )

    # Enter missing dates for Rashad Evans
    out.loc[(out["fighter"] == "Rashad Evans") & (out["record"] == "4–0"), "date"] = (
        "June 3, 2004"
    )

    out.loc[(out["fighter"] == "Rashad Evans") & (out["record"] == "1–0"), "date"] = (
        "April 10, 2004"
    )

    # Enter missing dates for Rashid Magomedov
    out.loc[
        (out["fighter"] == "Rashid Magomedov") & (out["record"] == "21–2–1"), "date"
    ] = "October 13, 2018"

    # Enter missing dates for Remco Pardoel
    out.loc[
        (out["fighter"] == "Remco Pardoel") & (out["record"] == "4–2 (1)"), "date"
    ] = "8 September 1995"

    out.loc[(out["fighter"] == "Remco Pardoel") & (out["record"] == "2–0"), "date"] = (
        "11 March 1994"
    )

    out.loc[(out["fighter"] == "Remco Pardoel") & (out["record"] == "1–0"), "date"] = (
        "11 March 1994"
    )

    # Enter missing dates for Renzo Gracie
    out.loc[
        (out["fighter"] == "Renzo Gracie") & (out["record"] == "8–0–1 (1)"), "date"
    ] = "December 22, 1999"

    out.loc[(out["fighter"] == "Renzo Gracie") & (out["record"] == "3–0"), "date"] = (
        "October 17, 1995"
    )

    out.loc[(out["fighter"] == "Renzo Gracie") & (out["record"] == "2–0"), "date"] = (
        "October 17, 1995"
    )

    # Enter missing dates for Ricco Rodriguez
    out.loc[
        (out["fighter"] == "Ricco Rodriguez") & (out["record"] == "29–8"), "date"
    ] = "April 11, 2008"

    # Enter missing dates for Ricco Rodriguez
    out.loc[
        (out["fighter"] == "Ricco Rodriguez") & (out["record"] == "29–8"), "date"
    ] = "April 11, 2008"

    # Enter missing dates for Rin Nakai
    out.loc[(out["fighter"] == "Rin Nakai") & (out["record"] == "24–2–1"), "date"] = (
        "May 8, 2022"
    )

    # Enter missing dates for Rinat Fakhretdinov
    out.loc[
        (out["fighter"] == "Rinat Fakhretdinov") & (out["record"] == "1–0"), "date"
    ] = "June 5, 2013"

    # Enter missing dates for Roan Carneiro
    out.loc[(out["fighter"] == "Roan Carneiro") & (out["record"] == "18–9"), "date"] = (
        "4 October 2014"
    )

    out.loc[(out["fighter"] == "Roan Carneiro") & (out["record"] == "17–9"), "date"] = (
        "4 October 2014"
    )

    out.loc[(out["fighter"] == "Roan Carneiro") & (out["record"] == "8–3"), "date"] = (
        "18 March 2006"
    )

    out.loc[(out["fighter"] == "Roan Carneiro") & (out["record"] == "7–3"), "date"] = (
        "18 March 2006"
    )

    # Enter missing dates for Roger Huerta
    out.loc[(out["fighter"] == "Roger Huerta") & (out["record"] == "9–1–1"), "date"] = (
        "March 5, 2005"
    )

    out.loc[(out["fighter"] == "Roger Huerta") & (out["record"] == "8–1–1"), "date"] = (
        "March 5, 2005"
    )

    out.loc[(out["fighter"] == "Roger Huerta") & (out["record"] == "4–0–1"), "date"] = (
        "June 18, 2004"
    )

    out.loc[(out["fighter"] == "Roger Huerta") & (out["record"] == "3–0–1"), "date"] = (
        "June 18, 2004"
    )

    out.loc[(out["fighter"] == "Roger Huerta") & (out["record"] == "1–0"), "date"] = (
        "August 2, 2003"
    )

    # Enter missing dates for Rogério Bontorin
    out.loc[
        (out["fighter"] == "Rogério Bontorin") & (out["record"] == "9–0"), "date"
    ] = "23 July 2016"

    # Enter missing dates for Rogério Bontorin
    out.loc[
        (out["fighter"] == "Rogério Bontorin") & (out["record"] == "9–0"), "date"
    ] = "23 July 2016"

    # Enter missing dates for Roy Nelson
    out.loc[(out["fighter"] == "Roy Nelson") & (out["record"] == "1–0"), "date"] = (
        "April 17, 2004"
    )

    # Enter missing dates for Royce Gracie
    out.loc[(out["fighter"] == "Royce Gracie") & (out["record"] == "10–0"), "date"] = (
        "December 16, 1994"
    )

    out.loc[(out["fighter"] == "Royce Gracie") & (out["record"] == "9–0"), "date"] = (
        "December 16, 1994"
    )

    out.loc[(out["fighter"] == "Royce Gracie") & (out["record"] == "6–0"), "date"] = (
        "March 11, 1994"
    )

    out.loc[(out["fighter"] == "Royce Gracie") & (out["record"] == "5–0"), "date"] = (
        "March 11, 1994"
    )

    out.loc[(out["fighter"] == "Royce Gracie") & (out["record"] == "4–0"), "date"] = (
        "March 11, 1994"
    )

    out.loc[(out["fighter"] == "Royce Gracie") & (out["record"] == "2–0"), "date"] = (
        "November 12, 1993"
    )

    out.loc[(out["fighter"] == "Royce Gracie") & (out["record"] == "1–0"), "date"] = (
        "November 12, 1993"
    )

    # Enter missing dates for Santiago Ponzinibbio
    out.loc[
        (out["fighter"] == "Santiago Ponzinibbio") & (out["record"] == "16–1"), "date"
    ] = "March 2, 2012"

    out.loc[
        (out["fighter"] == "Santiago Ponzinibbio") & (out["record"] == "12–1"), "date"
    ] = "September 17, 2011"

    # Enter missing dates for Seo Hee Ham
    out.loc[(out["fighter"] == "Seo Hee Ham") & (out["record"] == "7–3"), "date"] = (
        "December 17, 2010"
    )

    # Enter missing dates for Shonie Carter
    out.loc[
        (out["fighter"] == "Shonie Carter") & (out["record"] == "16–3–5"), "date"
    ] = "September 24, 2000"

    out.loc[
        (out["fighter"] == "Shonie Carter") & (out["record"] == "5–1–1"), "date"
    ] = "March 6, 1998"

    out.loc[
        (out["fighter"] == "Shonie Carter") & (out["record"] == "2–1–1"), "date"
    ] = "April 18, 1997"

    # Enter missing dates for Steve Berger
    out.loc[
        (out["fighter"] == "Steve Berger") & (out["record"] == "9–4–1 (1)"), "date"
    ] = "October 6, 2000"

    out.loc[
        (out["fighter"] == "Steve Berger") & (out["record"] == "5–2 (1)"), "date"
    ] = "November 6, 1999"

    out.loc[(out["fighter"] == "Steve Berger") & (out["record"] == "3–0"), "date"] = (
        "May 2, 1998"
    )

    # Enter missing dates for Steven Siler
    out.loc[
        (out["fighter"] == "Steven Siler") & (out["record"] == "31–17–1"), "date"
    ] = "October 5, 2018"

    # Enter missing dates for Tank Abbott
    out.loc[(out["fighter"] == "Tank Abbott") & (out["record"] == "6–3"), "date"] = (
        "December 7, 1996"
    )

    out.loc[(out["fighter"] == "Tank Abbott") & (out["record"] == "5–3"), "date"] = (
        "December 7, 1996"
    )

    out.loc[(out["fighter"] == "Tank Abbott") & (out["record"] == "4–2"), "date"] = (
        "September 20, 1996"
    )

    out.loc[(out["fighter"] == "Tank Abbott") & (out["record"] == "3–1"), "date"] = (
        "December 16, 1995"
    )

    out.loc[(out["fighter"] == "Tank Abbott") & (out["record"] == "2–0"), "date"] = (
        "July 14, 1995"
    )

    out.loc[(out["fighter"] == "Tank Abbott") & (out["record"] == "1–0"), "date"] = (
        "July 14, 1995"
    )

    # Enter missing dates for Taylor Lapilus
    out.loc[(out["fighter"] == "Taylor Lapilus") & (out["record"] == "2–0"), "date"] = (
        "November 10, 2012"
    )

    # Enter missing dates for Thiago Tavares
    out.loc[
        (out["fighter"] == "Thiago Tavares") & (out["record"] == "22–9–1"), "date"
    ] = "October 13, 2018"

    # Enter missing dates for Thibault Gouti
    out.loc[(out["fighter"] == "Thibault Gouti") & (out["record"] == "8–0"), "date"] = (
        "10 May 2014"
    )

    # Enter missing dates for Tim Sylvia
    out.loc[(out["fighter"] == "Tim Sylvia") & (out["record"] == "11–0"), "date"] = (
        "April 27, 2002"
    )

    out.loc[(out["fighter"] == "Tim Sylvia") & (out["record"] == "10–0"), "date"] = (
        "April 27, 2002"
    )

    out.loc[(out["fighter"] == "Tim Sylvia") & (out["record"] == "7–0"), "date"] = (
        "March 16, 2002"
    )

    out.loc[(out["fighter"] == "Tim Sylvia") & (out["record"] == "6–0"), "date"] = (
        "March 16, 2002"
    )

    # Enter missing dates for Tito Ortiz
    out.loc[(out["fighter"] == "Tito Ortiz") & (out["record"] == "1–0"), "date"] = (
        "May 30, 1997"
    )

    # Enter missing dates for Tony Fryklund
    out.loc[(out["fighter"] == "Tony Fryklund") & (out["record"] == "1–0"), "date"] = (
        "July 27, 1997"
    )

    # Enter missing dates for Travis Wiuff
    out.loc[(out["fighter"] == "Travis Wiuff") & (out["record"] == "6–1"), "date"] = (
        "March 16, 2002"
    )

    out.loc[(out["fighter"] == "Travis Wiuff") & (out["record"] == "4–1"), "date"] = (
        "March 8, 2002"
    )

    out.loc[(out["fighter"] == "Travis Wiuff") & (out["record"] == "3–0"), "date"] = (
        "February 16, 2002"
    )

    # Enter missing dates for Vinny Magalhaes
    out.loc[
        (out["fighter"] == "Vinny Magalhaes") & (out["record"] == "17–9 (1)"), "date"
    ] = "October 13, 2018"

    # Enter missing dates for Vinny Magalhães
    out.loc[
        (out["fighter"] == "Vinny Magalhães") & (out["record"] == "17–9 (1)"), "date"
    ] = "October 13, 2018"

    # Enter missing dates for Vitor Belfort
    out.loc[(out["fighter"] == "Vitor Belfort") & (out["record"] == "2–0"), "date"] = (
        "7 February 1997"
    )

    # Enter missing dates for Wanderlei Silva
    out.loc[
        (out["fighter"] == "Wanderlei Silva") & (out["record"] == "23–3–1 (1)"), "date"
    ] = "9 November 2003"

    out.loc[
        (out["fighter"] == "Wanderlei Silva") & (out["record"] == "4–0"), "date"
    ] = "15 September 1997"

    out.loc[
        (out["fighter"] == "Wanderlei Silva") & (out["record"] == "3–0"), "date"
    ] = "15 September 1997"

    # Enter missing dates for Yazmin Jauregui
    out.loc[
        (out["fighter"] == "Yazmin Jauregui") & (out["record"] == "7–0"), "date"
    ] = "August 13, 2021"

    out.loc[
        (out["fighter"] == "Yazmin Jauregui") & (out["record"] == "6–0"), "date"
    ] = "August 13, 2021"

    # Enter missing dates for Yoshihiro Akiyama
    out.loc[
        (out["fighter"] == "Yoshihiro Akiyama") & (out["record"] == "8–1"), "date"
    ] = "October 9, 2006"

    # Enter missing dates for Yui Chul Nam
    out.loc[(out["fighter"] == "Yui Chul Nam") & (out["record"] == "6–0"), "date"] = (
        "November 4, 2006"
    )

    out.loc[(out["fighter"] == "Yui Chul Nam") & (out["record"] == "3–0"), "date"] = (
        "April 22, 2006"
    )

    out.loc[(out["fighter"] == "Yui Chul Nam") & (out["record"] == "1–0"), "date"] = (
        "February 11, 2006"
    )

    # Enter missing dates for Zhalgas Zhumagulov
    out.loc[
        (out["fighter"] == "Zhalgas Zhumagulov") & (out["record"] == "5–0"), "date"
    ] = "October 6, 2014"

    out.loc[
        (out["fighter"] == "Zhalgas Zhumagulov") & (out["record"] == "4–0"), "date"
    ] = "October 6, 2014"

    out.loc[
        (out["fighter"] == "Zhalgas Zhumagulov") & (out["record"] == "3–0"), "date"
    ] = "October 6, 2014"

    # Enter missing dates for Zhang Mingyang
    out.loc[
        (out["fighter"] == "Zhang Mingyang") & (out["record"] == "13–6"), "date"
    ] = "January 14, 2021"

    out.loc[
        (out["fighter"] == "Zhang Mingyang") & (out["record"] == "10–6"), "date"
    ] = "September 5, 2020"

    out.loc[(out["fighter"] == "Zhang Mingyang") & (out["record"] == "9–6"), "date"] = (
        "September 5, 2020"
    )

    # Enter missing dates for Bazigit Atajev
    out.loc[
        (out["fighter"] == "Bazigit Atajev") & (out["record"] == "20–4–1"), "date"
    ] = "October 31, 2019"

    out.loc[
        (out["fighter"] == "Bazigit Atajev") & (out["record"] == "19–2"), "date"
    ] = "October 13, 2018"

    out.loc[(out["fighter"] == "Bazigit Atajev") & (out["record"] == "5–0"), "date"] = (
        "February 8, 2001"
    )

    out.loc[(out["fighter"] == "Bazigit Atajev") & (out["record"] == "4–0"), "date"] = (
        "February 8, 2001"
    )

    out.loc[(out["fighter"] == "Bazigit Atajev") & (out["record"] == "3–0"), "date"] = (
        "February 8, 2001"
    )

    # Enter missing dates for Fedor Emelianenko
    out.loc[
        (out["fighter"] == "Fedor Emelianenko") & (out["record"] == "20–1"), "date"
    ] = "August 15, 2004"

    out.loc[
        (out["fighter"] == "Fedor Emelianenko") & (out["record"] == "4–0"), "date"
    ] = "December 22, 2000"

    # Enter missing dates for Igor Vovchanchyn
    out.loc[
        (out["fighter"] == "Igor Vovchanchyn") & (out["record"] == "42–2 (1)"), "date"
    ] = "May 1, 2000"

    out.loc[
        (out["fighter"] == "Igor Vovchanchyn") & (out["record"] == "41–2 (1)"), "date"
    ] = "May 1, 2000"

    out.loc[
        (out["fighter"] == "Igor Vovchanchyn") & (out["record"] == "30–2"), "date"
    ] = "February 3, 1998"

    out.loc[
        (out["fighter"] == "Igor Vovchanchyn") & (out["record"] == "29–2"), "date"
    ] = "February 3, 1998"

    out.loc[
        (out["fighter"] == "Igor Vovchanchyn") & (out["record"] == "27–2"), "date"
    ] = "November 12, 1997"

    out.loc[
        (out["fighter"] == "Igor Vovchanchyn") & (out["record"] == "26–2"), "date"
    ] = "November 12, 1997"

    out.loc[
        (out["fighter"] == "Igor Vovchanchyn") & (out["record"] == "16–2"), "date"
    ] = "March 30, 1996"

    out.loc[
        (out["fighter"] == "Igor Vovchanchyn") & (out["record"] == "15–2"), "date"
    ] = "March 30, 1996"

    out.loc[
        (out["fighter"] == "Igor Vovchanchyn") & (out["record"] == "10–2"), "date"
    ] = "March 1, 1996"

    out.loc[
        (out["fighter"] == "Igor Vovchanchyn") & (out["record"] == "9–2"), "date"
    ] = "March 1, 1996"

    out.loc[
        (out["fighter"] == "Igor Vovchanchyn") & (out["record"] == "7–2"), "date"
    ] = "January 23, 1996"

    out.loc[
        (out["fighter"] == "Igor Vovchanchyn") & (out["record"] == "6–2"), "date"
    ] = "January 23, 1996"

    out.loc[
        (out["fighter"] == "Igor Vovchanchyn") & (out["record"] == "5–1"), "date"
    ] = "November 25, 1995"

    out.loc[
        (out["fighter"] == "Igor Vovchanchyn") & (out["record"] == "4–1"), "date"
    ] = "November 25, 1995"

    out.loc[
        (out["fighter"] == "Igor Vovchanchyn") & (out["record"] == "3–1"), "date"
    ] = "November 25, 1995"

    out.loc[
        (out["fighter"] == "Igor Vovchanchyn") & (out["record"] == "2–0"), "date"
    ] = "October 14, 1995"

    out.loc[
        (out["fighter"] == "Igor Vovchanchyn") & (out["record"] == "1–0"), "date"
    ] = "October 14, 1995"

    # Enter missing dates for Kiyoshi Tamura
    out.loc[
        (out["fighter"] == "Kiyoshi Tamura") & (out["record"] == "23–5–3"), "date"
    ] = "October 9, 2000"

    out.loc[
        (out["fighter"] == "Kiyoshi Tamura") & (out["record"] == "20–3–3"), "date"
    ] = "February 26, 2000"

    out.loc[
        (out["fighter"] == "Kiyoshi Tamura") & (out["record"] == "18–3–3"), "date"
    ] = "December 22, 1999"

    # Enter missing dates for Masakazu Imanari
    out.loc[
        (out["fighter"] == "Masakazu Imanari") & (out["record"] == "22–8–2"), "date"
    ] = "May 29, 2011"

    out.loc[
        (out["fighter"] == "Masakazu Imanari") & (out["record"] == "8–4–2"), "date"
    ] = "December 2, 2005"

    # Enter missing dates for Mirko Filipović
    out.loc[
        (out["fighter"] == "Mirko Filipović") & (out["record"] == "34–11–2 (1)"), "date"
    ] = "December 31, 2016"

    out.loc[
        (out["fighter"] == "Mirko Filipović") & (out["record"] == "20–4–2"), "date"
    ] = "September 10, 2006"

    # Enter missing dates for Ricardo Morais
    out.loc[(out["fighter"] == "Ricardo Morais") & (out["record"] == "4–0"), "date"] = (
        "November 25, 1995"
    )

    out.loc[(out["fighter"] == "Ricardo Morais") & (out["record"] == "3–0"), "date"] = (
        "November 25, 1995"
    )

    out.loc[(out["fighter"] == "Ricardo Morais") & (out["record"] == "2–0"), "date"] = (
        "November 25, 1995"
    )

    out.loc[(out["fighter"] == "Ricardo Morais") & (out["record"] == "1–0"), "date"] = (
        "November 25, 1995"
    )

    # Enter missing dates for Rickson Gracie
    out.loc[(out["fighter"] == "Rickson Gracie") & (out["record"] == "7–0"), "date"] = (
        "April 20, 1995"
    )

    out.loc[(out["fighter"] == "Rickson Gracie") & (out["record"] == "6–0"), "date"] = (
        "April 20, 1995"
    )

    out.loc[(out["fighter"] == "Rickson Gracie") & (out["record"] == "4–0"), "date"] = (
        "July 29, 1994"
    )

    out.loc[(out["fighter"] == "Rickson Gracie") & (out["record"] == "3–0"), "date"] = (
        "July 29, 1994"
    )

    # Enter missing dates for Sergei Kharitonov
    out.loc[
        (out["fighter"] == "Sergei Kharitonov") & (out["record"] == "5–0"), "date"
    ] = "February 20, 2003"

    out.loc[
        (out["fighter"] == "Sergei Kharitonov") & (out["record"] == "2–0"), "date"
    ] = "August 11, 2000"

    out.loc[
        (out["fighter"] == "Sergei Kharitonov") & (out["record"] == "1–0"), "date"
    ] = "August 11, 2000"

    # Enter missing dates for Shinya Aoki
    out.loc[
        (out["fighter"] == "Shinya Aoki") & (out["record"] == "17–2 (1)"), "date"
    ] = "July 21, 2008"

    out.loc[(out["fighter"] == "Shinya Aoki") & (out["record"] == "1–0"), "date"] = (
        "November 24, 2003"
    )

    # Enter missing dates for Valentijn Overeem
    out.loc[
        (out["fighter"] == "Valentijn Overeem") & (out["record"] == "23–19"), "date"
    ] = "12 December 2003"

    out.loc[
        (out["fighter"] == "Valentijn Overeem") & (out["record"] == "22–19"), "date"
    ] = "12 December 2003"

    out.loc[
        (out["fighter"] == "Valentijn Overeem") & (out["record"] == "19–9"), "date"
    ] = "24 February 2001"

    out.loc[
        (out["fighter"] == "Valentijn Overeem") & (out["record"] == "18–9"), "date"
    ] = "24 February 2001"

    out.loc[
        (out["fighter"] == "Valentijn Overeem") & (out["record"] == "15–9"), "date"
    ] = "9 October 2000"

    out.loc[
        (out["fighter"] == "Valentijn Overeem") & (out["record"] == "12–9"), "date"
    ] = "22 July 2000"

    # Enter missing dates for Yoshiro Maeda
    out.loc[
        (out["fighter"] == "Yoshiro Maeda") & (out["record"] == "17–1–1"), "date"
    ] = "December 2, 2005"

    # Enter missing dates for Gesias Cavalcante
    out.loc[
        (out["fighter"] == "Gesias Cavalcante") & (out["record"] == "13–1–1"), "date"
    ] = "September 17, 2007"

    out.loc[
        (out["fighter"] == "Gesias Cavalcante") & (out["record"] == "10–1–1"), "date"
    ] = "October 9, 2006"

    # Enter missing dates for Muhammed Lawal
    out.loc[
        (out["fighter"] == "Muhammed Lawal") & (out["record"] == "18–4 (1)"), "date"
    ] = "December 31, 2015"

    # Enter missing dates for Louis Taylor
    out.loc[(out["fighter"] == "Louis Taylor") & (out["record"] == "17–4"), "date"] = (
        "October 20, 2018"
    )

    # Enter missing dates for Alexander Sarnavskiy
    out.loc[
        (out["fighter"] == "Alexander Sarnavskiy") & (out["record"] == "7–0"), "date"
    ] = "February 13, 2010"

    out.loc[
        (out["fighter"] == "Alexander Sarnavskiy") & (out["record"] == "3–0"), "date"
    ] = "July 2, 2009"

    # Enter missing dates for Luis Palomino
    out.loc[
        (out["fighter"] == "Luis Palomino") & (out["record"] == "24–11"), "date"
    ] = "November 20, 2015"

    # Enter missing dates for Valesca Machado
    out.loc[
        (out["fighter"] == "Valesca Machado") & (out["record"] == "11–3 (1)"), "date"
    ] = "November 16, 2022"

    # Enter missing dates for Ray Cooper III
    out.loc[
        (out["fighter"] == "Ray Cooper III") & (out["record"] == "18–7–1"), "date"
    ] = "October 11, 2019"

    out.loc[
        (out["fighter"] == "Ray Cooper III") & (out["record"] == "16–5"), "date"
    ] = "October 20, 2018"

    # Enter missing dates for Denis Goltsov
    out.loc[(out["fighter"] == "Denis Goltsov") & (out["record"] == "25–5"), "date"] = (
        "October 31, 2019"
    )

    # Enter missing dates for Magomed Magomedkerimov
    out.loc[
        (out["fighter"] == "Magomed Magomedkerimov") & (out["record"] == "22–5"), "date"
    ] = "October 20, 2018"

    out.loc[
        (out["fighter"] == "Magomed Magomedkerimov") & (out["record"] == "4–1"), "date"
    ] = "September 26, 2011"

    # Enter missing dates for Sadibou Sy
    out.loc[(out["fighter"] == "Sadibou Sy") & (out["record"] == "7–3–1"), "date"] = (
        "October 20, 2018"
    )

    # Enter missing dates for Hiromasa Ougikubo
    out.loc[
        (out["fighter"] == "Hiromasa Ougikubo") & (out["record"] == "24–5–2"), "date"
    ] = "December 31, 2021"

    # Enter missing dates for Rena Kubota
    out.loc[(out["fighter"] == "Rena Kubota") & (out["record"] == "6–0"), "date"] = (
        "December 31, 2017"
    )

    # Enter missing dates for Saori Oshima
    out.loc[(out["fighter"] == "Saori Oshima") & (out["record"] == "5–2"), "date"] = (
        "June 20, 2021"
    )

    # Enter missing dates for Tofiq Musayev
    out.loc[(out["fighter"] == "Tofiq Musayev") & (out["record"] == "18–3"), "date"] = (
        "December 31, 2019"
    )

    out.loc[(out["fighter"] == "Tofiq Musayev") & (out["record"] == "8–3"), "date"] = (
        "June 5, 2016"
    )

    # Enter missing dates for Hideo Tokoro
    out.loc[
        (out["fighter"] == "Hideo Tokoro") & (out["record"] == "28–23–2"), "date"
    ] = "May 29, 2011"

    # Enter missing dates for Alex Nicholson
    out.loc[
        (out["fighter"] == "Alex Nicholson") & (out["record"] == "13–6"), "date"
    ] = "October 5, 2018"

    # Enter missing dates for Alexander Yakovlev
    out.loc[
        (out["fighter"] == "Alexander Yakovlev") & (out["record"] == "1–0"), "date"
    ] = "19 February 2004"

    # Enter missing dates for Brian Foster
    out.loc[(out["fighter"] == "Brian Foster") & (out["record"] == "25–8"), "date"] = (
        "November 20, 2015"
    )

    out.loc[(out["fighter"] == "Brian Foster") & (out["record"] == "24–8"), "date"] = (
        "November 20, 2015"
    )

    # Enter missing dates for Bruno Silva
    out.loc[(out["fighter"] == "Bruno Silva") & (out["record"] == "8–5"), "date"] = (
        "July 6, 2013"
    )

    # Enter missing dates for Chris Curtis
    out.loc[(out["fighter"] == "Chris Curtis") & (out["record"] == "21–7"), "date"] = (
        "October 11, 2019"
    )

    # Enter missing dates for Chris Wade
    out.loc[(out["fighter"] == "Chris Wade") & (out["record"] == "17–5"), "date"] = (
        "October 17, 2019"
    )

    out.loc[(out["fighter"] == "Chris Wade") & (out["record"] == "14–4"), "date"] = (
        "October 13, 2018"
    )

    # Enter missing dates for Danny Roberts
    out.loc[(out["fighter"] == "Danny Roberts") & (out["record"] == "6–0"), "date"] = (
        "16 December 2011"
    )

    # Enter missing dates for Diego Rivas
    out.loc[(out["fighter"] == "Diego Rivas") & (out["record"] == "3–0"), "date"] = (
        "December 10, 2011"
    )

    # Enter missing dates for Francisco Rivera
    out.loc[
        (out["fighter"] == "Francisco Rivera") & (out["record"] == "14–7 (1)"), "date"
    ] = "May 29, 2021"

    out.loc[
        (out["fighter"] == "Francisco Rivera") & (out["record"] == "13–7 (1)"), "date"
    ] = "May 29, 2021"

    # Enter missing dates for Javier Vazquez
    out.loc[(out["fighter"] == "Javier Vazquez") & (out["record"] == "2–0"), "date"] = (
        "June 28, 1998"
    )

    out.loc[(out["fighter"] == "Javier Vazquez") & (out["record"] == "1–0"), "date"] = (
        "June 28, 1998"
    )

    # Enter missing dates for John Allan
    out.loc[(out["fighter"] == "John Allan") & (out["record"] == "7–3"), "date"] = (
        "March 24, 2016"
    )

    # Enter missing dates for John Howard
    out.loc[(out["fighter"] == "John Howard") & (out["record"] == "27–14"), "date"] = (
        "October 20, 2018"
    )

    # Enter missing dates for Jordan Johnson
    out.loc[
        (out["fighter"] == "Jordan Johnson") & (out["record"] == "11–1–1"), "date"
    ] = "October 31, 2019"

    # Enter missing dates for Manuel Torres
    out.loc[(out["fighter"] == "Manuel Torres") & (out["record"] == "7–0"), "date"] = (
        "August 18, 2018"
    )

    # Enter missing dates for Manuel Torres
    out.loc[(out["fighter"] == "Manuel Torres") & (out["record"] == "7–0"), "date"] = (
        "August 18, 2018"
    )

    # Enter missing dates for Mark Hall
    out.loc[(out["fighter"] == "Mark Hall") & (out["record"] == "5–4"), "date"] = (
        "September 15, 1997"
    )

    out.loc[(out["fighter"] == "Mark Hall") & (out["record"] == "1–0"), "date"] = (
        "September 8, 1995"
    )

    # Enter missing dates for Mark Kerr
    out.loc[(out["fighter"] == "Mark Kerr") & (out["record"] == "6–0"), "date"] = (
        "October 17, 1997"
    )

    out.loc[(out["fighter"] == "Mark Kerr") & (out["record"] == "4–0"), "date"] = (
        "July 27, 199"
    )

    out.loc[(out["fighter"] == "Mark Kerr") & (out["record"] == "2–0"), "date"] = (
        "January 19, 1997"
    )

    out.loc[(out["fighter"] == "Mark Kerr") & (out["record"] == "1–0"), "date"] = (
        "January 19, 1997"
    )

    # Enter missing dates for Patrick Smith
    out.loc[(out["fighter"] == "Patrick Smith") & (out["record"] == "3–1"), "date"] = (
        "March 11, 1994"
    )

    out.loc[(out["fighter"] == "Patrick Smith") & (out["record"] == "2–1"), "date"] = (
        "March 11, 1994"
    )

    out.loc[(out["fighter"] == "Patrick Smith") & (out["record"] == "1–1"), "date"] = (
        "March 11, 1994"
    )

    # Enter missing dates for Phil Davis
    out.loc[
        (out["fighter"] == "Phil Davis") & (out["record"] == "14–3 (1)"), "date"
    ] = "September 19, 2015"

    # Enter missing dates for Sam Adkins
    out.loc[(out["fighter"] == "Sam Adkins") & (out["record"] == "6–16–1"), "date"] = (
        "February 1, 2003"
    )

    out.loc[(out["fighter"] == "Sam Adkins") & (out["record"] == "3–4"), "date"] = (
        "February 20, 1998"
    )

    out.loc[(out["fighter"] == "Sam Adkins") & (out["record"] == "1–0"), "date"] = (
        "February 16, 1996"
    )

    # Enter missing dates for Sean O'Connell
    out.loc[
        (out["fighter"] == "Sean O'Connell") & (out["record"] == "19–10"), "date"
    ] = "October 13, 2018"

    # Enter missing dates for Stevie Ray
    out.loc[(out["fighter"] == "Stevie Ray") & (out["record"] == "13–4"), "date"] = (
        "October 5, 2013"
    )

    out.loc[(out["fighter"] == "Stevie Ray") & (out["record"] == "7–1"), "date"] = (
        "June 18, 2011"
    )

    out.loc[(out["fighter"] == "Stevie Ray") & (out["record"] == "3–0"), "date"] = (
        "October 10, 2010"
    )

    # Enter missing dates for Daisuke Nakamura
    out.loc[
        (out["fighter"] == "Daisuke Nakamura") & (out["record"] == "8–5"), "date"
    ] = "October 30, 2004"

    out.loc[
        (out["fighter"] == "Daisuke Nakamura") & (out["record"] == "2–1"), "date"
    ] = "December 8, 2002"

    # Enter missing dates for Rafael Silva
    out.loc[(out["fighter"] == "Rafael Silva") & (out["record"] == "12–3"), "date"] = (
        "October 1, 2011"
    )

    # Enter missing dates for Aleksei Oleinik
    out.loc[
        (out["fighter"] == "Aleksei Oleinik") & (out["record"] == "4-0"), "date"
    ] = "April 30, 1997"

    # Enter missing dates for Alexey Oleynik
    out.loc[(out["fighter"] == "Alexey Oleynik") & (out["record"] == "4-0"), "date"] = (
        "April 30, 1997"
    )

    # Enter missing dates for Bojan Veličković
    out.loc[
        (out["fighter"] == "Bojan Veličković") & (out["record"] == "4-0"), "date"
    ] = "June 19, 2011"

    # Enter missing dates for Charles Oliveira
    out.loc[
        (out["fighter"] == "Charles Oliveira") & (out["record"] == "5-0"), "date"
    ] = "December 29, 2008"

    # Enter missing dates for Daniel Omielańczuk
    out.loc[
        (out["fighter"] == "Daniel Omielańczuk") & (out["record"] == "13–3–1 (1)"),
        "date",
    ] = "November 9, 2012"

    # Enter missing dates for Enrique Barzola
    out.loc[
        (out["fighter"] == "Enrique Barzola") & (out["record"] == "7–0-1"), "date"
    ] = "February 4, 2014"

    # Enter missing dates for Francisco Figueiredo
    out.loc[
        (out["fighter"] == "Francisco Figueiredo") & (out["record"] == "3–0"), "date"
    ] = "August 12, 2010"

    # Enter missing dates for Alex Stiebling
    out.loc[
        (out["fighter"] == "Alex Stiebling") & (out["record"] == "2–0–1"), "date"
    ] = "July 24, 1999"

    # Enter missing dates for Anderson Silva
    out.loc[(out["fighter"] == "Anderson Silva") & (out["record"] == "1–0"), "date"] = (
        "June 25, 1997"
    )

    # Enter missing dates for Anthony Birchak
    out.loc[
        (out["fighter"] == "Anthony Birchak") & (out["record"] == "16–6"), "date"
    ] = "October 11, 2019"

    # Enter missing dates for Bartosz Fabiński
    out.loc[
        (out["fighter"] == "Bartosz Fabiński") & (out["record"] == "10–2"), "date"
    ] = "June 8, 2014"

    # Enter missing dates for Brad Katona
    out.loc[(out["fighter"] == "Brad Katona") & (out["record"] == "5–0"), "date"] = (
        "February 1, 2017"
    )

    # Enter missing dates for Bubba McDaniel
    out.loc[
        (out["fighter"] == "Bubba McDaniel") & (out["record"] == "10–4"), "date"
    ] = "March 15, 2008"

    out.loc[(out["fighter"] == "Bubba McDaniel") & (out["record"] == "3–1"), "date"] = (
        "March 10, 2006"
    )

    # Enter missing dates for Damian Grabowski
    out.loc[
        (out["fighter"] == "Damian Grabowski") & (out["record"] == "19–1"), "date"
    ] = "November 30, 2013"

    # Enter missing dates for Frankie Perez
    out.loc[(out["fighter"] == "Frankie Perez") & (out["record"] == "11–4"), "date"] = (
        "June 08, 2018"
    )

    out.loc[(out["fighter"] == "Frankie Perez") & (out["record"] == "10–4"), "date"] = (
        "July 22, 2017"
    )

    out.loc[(out["fighter"] == "Frankie Perez") & (out["record"] == "10–3"), "date"] = (
        "December 9, 2016"
    )

    out.loc[(out["fighter"] == "Frankie Perez") & (out["record"] == "10–2"), "date"] = (
        "August 23, 2015"
    )

    out.loc[(out["fighter"] == "Frankie Perez") & (out["record"] == "9–2"), "date"] = (
        "January 18, 2015"
    )

    out.loc[(out["fighter"] == "Frankie Perez") & (out["record"] == "9-1"), "date"] = (
        "June 28, 2014"
    )

    out.loc[(out["fighter"] == "Frankie Perez") & (out["record"] == "8-0"), "date"] = (
        "January 24, 2014"
    )

    out.loc[(out["fighter"] == "Frankie Perez") & (out["record"] == "7-0"), "date"] = (
        "September 20, 2013"
    )

    out.loc[(out["fighter"] == "Frankie Perez") & (out["record"] == "5-0"), "date"] = (
        "January 24, 2013"
    )

    out.loc[(out["fighter"] == "Frankie Perez") & (out["record"] == "4-0"), "date"] = (
        "June 15, 2012"
    )

    out.loc[(out["fighter"] == "Frankie Perez") & (out["record"] == "3-0"), "date"] = (
        "February 10, 2012"
    )

    out.loc[(out["fighter"] == "Frankie Perez") & (out["record"] == "2-0"), "date"] = (
        "November 18, 2011"
    )

    out.loc[(out["fighter"] == "Frankie Perez") & (out["record"] == "1-0"), "date"] = (
        "June 17, 2011"
    )

    # Enter missing dates for Gil Castillo
    out.loc[(out["fighter"] == "Gil Castillo") & (out["record"] == "3–0"), "date"] = (
        "September 28, 1998"
    )

    # Enter missing dates for Ikuhisa Minowa
    out.loc[
        (out["fighter"] == "Ikuhisa Minowa") & (out["record"] == "45–30–8"), "date"
    ] = "March 22, 2010"

    out.loc[
        (out["fighter"] == "Ikuhisa Minowa") & (out["record"] == "44–30–8"), "date"
    ] = "December 31, 2009"

    out.loc[
        (out["fighter"] == "Ikuhisa Minowa") & (out["record"] == "43–30–8"), "date"
    ] = "October 6, 2009"

    # Enter missing dates for Ivan Jorge
    out.loc[(out["fighter"] == "Ivan Jorge") & (out["record"] == "27–7"), "date"] = (
        "October 21, 2016"
    )

    # Enter missing dates for Jarjis Danho
    out.loc[
        (out["fighter"] == "Jarjis Danho") & (out["record"] == "4–0 (1)"), "date"
    ] = "February 28, 2015"

    out.loc[
        (out["fighter"] == "Jarjis Danho") & (out["record"] == "2–0 (1)"), "date"
    ] = "June 1, 2013"

    out.loc[(out["fighter"] == "Jarjis Danho") & (out["record"] == "1–0"), "date"] = (
        "September 22, 2012"
    )

    # Enter missing dates for Johnny Eduardo
    out.loc[(out["fighter"] == "Johnny Eduardo") & (out["record"] == "8–1"), "date"] = (
        "June 6, 1998"
    )

    out.loc[(out["fighter"] == "Johnny Eduardo") & (out["record"] == "5–1"), "date"] = (
        "August 30, 1997"
    )

    out.loc[(out["fighter"] == "Johnny Eduardo") & (out["record"] == "1–1"), "date"] = (
        "April 5, 1997"
    )

    # Enter missing dates for Junior Assuncao
    out.loc[
        (out["fighter"] == "Junior Assuncao") & (out["record"] == "7–4"), "date"
    ] = "November 8, 2008"

    # Enter missing dates for Junior Assunção
    out.loc[
        (out["fighter"] == "Junior Assunção") & (out["record"] == "7–4"), "date"
    ] = "November 8, 2008"

    # Enter missing dates for Júnior Assunção
    out.loc[
        (out["fighter"] == "Júnior Assunção") & (out["record"] == "7–4"), "date"
    ] = "November 8, 2008"

    # Enter missing dates for Kuniyoshi Hironaka
    out.loc[
        (out["fighter"] == "Kuniyoshi Hironaka") & (out["record"] == "16–7"), "date"
    ] = "March 22, 2010"

    # Enter missing dates for Maciej Jewtuszko
    out.loc[
        (out["fighter"] == "Maciej Jewtuszko") & (out["record"] == "12–5"), "date"
    ] = "June 15, 2019"

    # Enter missing dates for Ode' Osbourne
    out.loc[
        (out["fighter"] == "Ode' Osbourne") & (out["record"] == "3–1 (1)"), "date"
    ] = "June 17, 2016"

    # Enter missing dates for Pedro Rizzo
    out.loc[(out["fighter"] == "Pedro Rizzo") & (out["record"] == "17–9"), "date"] = (
        "September 12, 2009"
    )

    out.loc[(out["fighter"] == "Pedro Rizzo") & (out["record"] == "16–9"), "date"] = (
        "June 27, 2009"
    )

    out.loc[(out["fighter"] == "Pedro Rizzo") & (out["record"] == "16–8"), "date"] = (
        "July 19, 2008"
    )

    # Enter missing dates for Rameau Thierry Sokoudjou
    out.loc[
        (out["fighter"] == "Rameau Thierry Sokoudjou") & (out["record"] == "17–15"),
        "date",
    ] = "October 1, 2016"

    # Enter missing dates for Ryan Spann
    out.loc[(out["fighter"] == "Ryan Spann") & (out["record"] == "9–2"), "date"] = (
        "March 25, 2016"
    )

    out.loc[(out["fighter"] == "Ryan Spann") & (out["record"] == "8–2"), "date"] = (
        "November 13, 2015"
    )

    # Enter missing dates for Ryo Chonan
    out.loc[(out["fighter"] == "Ryo Chonan") & (out["record"] == "17–10"), "date"] = (
        "March 22, 2010"
    )

    # Enter missing dates for Shane Campbell
    out.loc[
        (out["fighter"] == "Shane Campbell") & (out["record"] == "16–7"), "date"
    ] = "December 15, 2018"

    # Enter missing dates for Terrion Ware
    out.loc[(out["fighter"] == "Terrion Ware") & (out["record"] == "13–3"), "date"] = (
        "February 6, 2015"
    )

    # Enter missing dates for Thiago Moisés
    out.loc[(out["fighter"] == "Thiago Moisés") & (out["record"] == "3–0"), "date"] = (
        "July 28, 2013"
    )

    # Enter missing dates for Travis Wiuff
    out.loc[(out["fighter"] == "Travis Wiuff") & (out["record"] == "45–10"), "date"] = (
        "July 14, 2007"
    )

    # Enter missing dates for Wilson Gouveia
    out.loc[
        (out["fighter"] == "Wilson Gouveia") & (out["record"] == "12–6"), "date"
    ] = "February 21, 2009"

    out.loc[
        (out["fighter"] == "Wilson Gouveia") & (out["record"] == "12–5"), "date"
    ] = "December 13, 2008"

    # Enter missing dates for Yasuhiro Urushitani
    out.loc[
        (out["fighter"] == "Yasuhiro Urushitani") & (out["record"] == "14–3–5"), "date"
    ] = "December 1, 2007"

    out.loc[
        (out["fighter"] == "Yasuhiro Urushitani") & (out["record"] == "0–1"), "date"
    ] = "January 19, 2001"

    # Enter missing dates for Zhang Lipeng
    out.loc[(out["fighter"] == "Zhang Lipeng") & (out["record"] == "6–5–1"), "date"] = (
        "December 1, 2012"
    )

    # Enter missing dates for Daniel Acácio
    out.loc[
        (out["fighter"] == "Daniel Acácio") & (out["record"] == "23–11"), "date"
    ] = "April 30, 2011"

    # Enter missing dates for Daniel Acácio
    out.loc[
        (out["fighter"] == "Daniel Acácio") & (out["record"] == "23–11"), "date"
    ] = "April 30, 2011"

    # Enter missing dates for Yoon Dong-Sik
    out.loc[(out["fighter"] == "Yoon Dong-Sik") & (out["record"] == "9–10"), "date"] = (
        "September 23, 2017"
    )

    # Enter missing dates for Yoshiro Maeda
    out.loc[
        (out["fighter"] == "Yoshiro Maeda") & (out["record"] == "24–6–2"), "date"
    ] = "March 8, 2009"

    # Enter missing dates for Bao Quach
    out.loc[(out["fighter"] == "Bao Quach") & (out["record"] == "15–9–1"), "date"] = (
        "Jan 24, 2009"
    )

    # Enter missing dates for Hideo Tokoro
    out.loc[
        (out["fighter"] == "Hideo Tokoro") & (out["record"] == "26–21–2"), "date"
    ] = "December 31, 2009"

    out.loc[
        (out["fighter"] == "Hideo Tokoro") & (out["record"] == "25–21–2"), "date"
    ] = "October 6, 2009"

    # Enter missing dates for Alex Perez
    out.loc[(out["fighter"] == "Alex Perez") & (out["record"] == "2–0"), "date"] = (
        "June 24, 2011"
    )

    # Enter missing dates for Damien Brown
    out.loc[(out["fighter"] == "Damien Brown") & (out["record"] == "6–3"), "date"] = (
        "February 11, 2012"
    )

    out.loc[(out["fighter"] == "Damien Brown") & (out["record"] == "3–0"), "date"] = (
        "December 18, 2010"
    )

    # Enter missing dates for Daniel Roberts
    out.loc[(out["fighter"] == "Daniel Roberts") & (out["record"] == "9–0"), "date"] = (
        "January 16, 2010"
    )

    out.loc[(out["fighter"] == "Daniel Roberts") & (out["record"] == "8–0"), "date"] = (
        "August 28, 2009"
    )

    # Enter missing dates for Jason Day
    out.loc[(out["fighter"] == "Jason Day") & (out["record"] == "3–5"), "date"] = (
        "April 9, 2005"
    )

    out.loc[(out["fighter"] == "Jason Day") & (out["record"] == "3–2"), "date"] = (
        "November 1, 2003"
    )

    # Enter missing dates for Jorge Rivera
    out.loc[(out["fighter"] == "Jorge Rivera") & (out["record"] == "5–1"), "date"] = (
        "November 30, 2002"
    )

    # Enter missing dates for Mark Kerr
    out.loc[(out["fighter"] == "Mark Kerr") & (out["record"] == "4–0"), "date"] = (
        "July 27, 1997"
    )

    # Enter missing dates for Mike Santiago
    out.loc[(out["fighter"] == "Mike Santiago") & (out["record"] == "7–5"), "date"] = (
        "March 17, 2012"
    )

    # Enter missing dates for Patrick Williams
    out.loc[
        (out["fighter"] == "Patrick Williams") & (out["record"] == "5–3"), "date"
    ] = "October 6, 2012"

    out.loc[
        (out["fighter"] == "Patrick Williams") & (out["record"] == "3–1"), "date"
    ] = "October 7, 2011"

    out.loc[
        (out["fighter"] == "Patrick Williams") & (out["record"] == "1–1"), "date"
    ] = "February 12, 2011"

    out.loc[
        (out["fighter"] == "Patrick Williams") & (out["record"] == "1–0"), "date"
    ] = "August 21, 2010"

    # Enter missing dates for Aleksei Oleinik
    out.loc[
        (out["fighter"] == "Aleksei Oleinik") & (out["record"] == "4–0"), "date"
    ] = "April 30, 1997"

    # Enter missing dates for Alexey Oleynik
    out.loc[(out["fighter"] == "Alexey Oleynik") & (out["record"] == "4–0"), "date"] = (
        "April 30, 1997"
    )

    # Enter missing dates for Bojan Veličković
    out.loc[
        (out["fighter"] == "Bojan Veličković") & (out["record"] == "3–0"), "date"
    ] = "June 19, 2011"

    # Enter missing dates for Daniel Omielańczuk
    out.loc[
        (out["fighter"] == "Daniel Omielańczuk") & (out["record"] == "13–3–1 (1)"),
        "date",
    ] = "November 9, 2012"

    # Enter missing dates for Enrique Barzola
    out.loc[
        (out["fighter"] == "Enrique Barzola") & (out["record"] == "7–0–1"), "date"
    ] = "February 4, 2014"

    # Enter missing dates for Francisco Figueiredo
    out.loc[
        (out["fighter"] == "Francisco Figueiredo") & (out["record"] == "3–0"), "date"
    ] = "August 12, 2010"

    # Enter missing dates for Michał Oleksiejczuk
    out.loc[
        (out["fighter"] == "Michał Oleksiejczuk") & (out["record"] == "6–2"), "date"
    ] = "September 26, 2015"

    # Enter missing dates for Rani Yahya
    out.loc[(out["fighter"] == "Rani Yahya") & (out["record"] == "3–0"), "date"] = (
        "April 17, 2004"
    )

    out.loc[(out["fighter"] == "Rani Yahya") & (out["record"] == "2–0"), "date"] = (
        "April 17, 2004"
    )

    # Enter missing dates for Wilson Gouveia
    out.loc[
        (out["fighter"] == "Wilson Gouveia") & (out["record"] == "11–5"), "date"
    ] = "September 17, 2008"

    # Enter missing dates for Igor Vovchanchyn
    out.loc[
        (out["fighter"] == "Igor Vovchanchyn") & (out["record"] == "36–2"), "date"
    ] = "May 8, 1999"

    out.loc[
        (out["fighter"] == "Igor Vovchanchyn") & (out["record"] == "21–2"), "date"
    ] = "May 23, 1997"

    out.loc[
        (out["fighter"] == "Igor Vovchanchyn") & (out["record"] == "13–2"), "date"
    ] = "March 9, 1996"

    out.loc[
        (out["fighter"] == "Igor Vovchanchyn") & (out["record"] == "12–2"), "date"
    ] = "March 9, 1996"

    # Enter missing dates for Kiyoshi Tamura
    out.loc[
        (out["fighter"] == "Kiyoshi Tamura") & (out["record"] == "11–2"), "date"
    ] = "January 21, 1998"

    out.loc[
        (out["fighter"] == "Kiyoshi Tamura") & (out["record"] == "10–2"), "date"
    ] = "January 21, 1998"

    out.loc[(out["fighter"] == "Kiyoshi Tamura") & (out["record"] == "5–0"), "date"] = (
        "January 1, 1997"
    )

    out.loc[(out["fighter"] == "Kiyoshi Tamura") & (out["record"] == "4–0"), "date"] = (
        "January 1, 1997"
    )

    # Enter missing dates for Murilo Rua
    out.loc[(out["fighter"] == "Murilo Rua") & (out["record"] == "16–9–1"), "date"] = (
        "October 4, 2008"
    )

    # Enter missing dates for Bao Quach
    out.loc[(out["fighter"] == "Bao Quach") & (out["record"] == "15–9–1"), "date"] = (
        "January 24, 2009"
    )

    # Enter missing dates for Magomed Umalatov
    out.loc[
        (out["fighter"] == "Magomed Umalatov") & (out["record"] == "5–0"), "date"
    ] = "September 8, 2018"

    out.loc[
        (out["fighter"] == "Magomed Umalatov") & (out["record"] == "4–0"), "date"
    ] = "September 8, 2018"

    # Enter missing dates for Matt Serra
    out.loc[
        (out["fighter"] == "Matt Serra")
        & (out["opponent"] == "Shonie Carter")
        & (out["record"] == "Exhibition"),
        "date",
    ] = "October 19, 2006"

    out.loc[
        (out["fighter"] == "Matt Serra")
        & (out["opponent"] == "Pete Spratt")
        & (out["record"] == "Exhibition"),
        "date",
    ] = "September 28, 2006"

    return out


def clean_fight_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    """
    Take the raw scraped fight history rows and return a cleaned version:
    - lowercase snake_case column names
    - rename result column to 'result'
    - create indicators for title fights and for finishes
    - apply manual corrections
    - drop rows with missing opponent or result
    -drop NC
    - reorder date strings and convert to datetime
    """

    if df.empty:
        return df.copy()

    out = df.copy()

    # standardize column names (lowercase, underscores)
    out.columns = [
        col.strip().lower().replace(" ", "_").replace("/", "_") for col in out.columns
    ]

    # rename result/res/res. column
    if "res." in out.columns:
        out = out.rename(columns={"res.": "result"})
    elif "res" in out.columns:
        out = out.rename(columns={"res": "result"})

    # championship_fight flag
    if "notes" in out.columns:
        championship = out["notes"].str.contains(
            r"championship|title|won", case=False, na=False
        )

        # define "high tier" championship fights
        if "event" in out.columns:
            high_tier = out["event"].str.contains(
                r"ufc|strikeforce|wec|pride",
                case=False,
                na=False,
            )
        else:
            high_tier = False

        out["high_tier_championship_fight"] = championship & high_tier
        out["low_tier_championship_fight"] = championship & ~high_tier
    else:
        out["high_tier_championship_fight"] = False
        out["low_tier_championship_fight"] = False

    # finish flag
    if "method" in out.columns:
        out["finish"] = out["method"].str.contains(
            r"submission|ko|tko", flags=re.IGNORECASE, na=False
        )
    else:
        out["finish"] = False

    # finally apply manual overrides
    out = _apply_manual_fixes(out)

    # Drop rows with missing opponent or result
    out = out.dropna(subset=["opponent", "result"])

    # Remove rows where 'result' contains 'NC'
    out = out[~out["result"].str.contains("NC", na=False)]

    # Reorder date string from for example '18 August 2024' to 'August 18, 2024'
    def reorder_date_string(s):
        match = re.match(r"^(\d{1,2}) (\w+) (\d{4})$", s.strip())
        if match:
            day, month, year = match.groups()
            return f"{month} {day}, {year}"
        return s  # return original if it doesn't match

    # Apply to new date column
    out["date_reordered"] = out["date"].astype(str).apply(reorder_date_string)

    # Convert date variable to datetime format
    out["date_fixed"] = pd.to_datetime(out["date_reordered"], errors="coerce")

    out["fight_sequence"] = out.groupby(
        ["fighter", "date_fixed"]
    ).cumcount()  # same fighter, same date

    out["datetime_adjusted"] = out["date_fixed"] + pd.to_timedelta(
        out["fight_sequence"], unit="s"
    )

    # Edit weights
    def extract_weight_lb(weight_str):
        match = re.search(r"\d+", str(weight_str))
        return int(match.group()) if match else None

    out["weight_lb"] = out["weight_info"].apply(extract_weight_lb)

    # Convert all weights less than or equal to 100 to pounds
    out["weight_lb"] = out["weight_lb"].apply(
        lambda x: round(x * 2.20462) if pd.notnull(x) and x <= 100 else x
    )

    # Edit gender variable
    out.loc[out["gender"].isna() & (out["weight_lb"] < 115), "gender"] = "female"

    # Drop unnecessary columns
    out = out.drop(
        columns=[
            "date",
            "round",
            "time",
            "location",
            "notes",
            "date_reordered",
            "date_fixed",
            "fight_sequence",
            "weather",
            "results",
        ]
    )

    # Rename cleaned columns
    out = out.rename(columns={"datetime_adjusted": "date"})

    # Sort by date (oldest to newest)
    out = out.sort_values(by="date").reset_index(drop=True)

    # Edit entries in results column
    out["result"].unique()

    out["result"] = out["result"].replace(
        {
            "loss": "Loss",
            "Lossx": "Loss",
            ":Loss": "Loss",
            "Lose": "Loss",
            "Winn": "Win",
            "Winx": "Win",
            "Wi": "Win",
            "Won": "Win",
            "win": "Win",
        }
    )

    return out
