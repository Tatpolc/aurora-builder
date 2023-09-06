from re import T
import sqlite3

class function:
    def import_apt(self):
        #connect to sqlite3 db
        conn = sqlite3.connect('navdata.sqlite')
        #create cursor
        c = conn.cursor()
        #open/create apt file
        apt_file = open("output\\VTBB.apt", "w")
        #execute sqlite3 command
        c.execute("""SELECT
        ident,
        altitude,
        transition_altitude,
        laty,
        lonx,
        name
        FROM airport
        WHERE region = "VT"
        """)
        #fetch all info from above
        airport = c.fetchall()
        #write apt
        for apt_item in airport:
            apt_file.write(apt_item[0]+';'+str(apt_item[1])+';'+str(apt_item[2])+';'+str(round(apt_item[3],10))+
            ';'+str(round(apt_item[4],9))+';'+apt_item[5]+';\n')
        print('Airport created successfully!')
        #close connection with database
        conn.close()

    def import_wpt(self):
        #connect to sqlite3 db
        conn = sqlite3.connect('navdata.sqlite')
        #create cursor
        c = conn.cursor()
        #open/create apt file
        wpt_file = open("output\\VTBB.wpt", "w")
        #execute sqlite3 command
        c.execute("""
            SELECT 
            waypoint.ident,
            waypoint.laty,
            waypoint.lonx,
            waypoint.arinc_type
            FROM
            waypoint
            WHERE
            waypoint.region = 'VT'
            AND
            waypoint.type = 'WN'
            """)
        #fetch all info from above
        waypoint = c.fetchall()
        #define type & boundary
        for wpt_item_tb in waypoint:
            #print(wpt_item_tb[3])
            if wpt_item_tb[3] in 'D''E''F''Z':
                print(wpt_item_tb[3])
        #write wpt
        for wpt_item in waypoint:
            wpt_file.write(wpt_item[0]+';'+str(wpt_item[1])+';'+str(wpt_item[2])+';'+'0;0;\n')

        c.execute("""
            SELECT DISTINCT
            T1.ident,
            T1.arinc_type,
            T1.type,
            T1.laty,
            T1.lonx,
            T1.region,	
            T1.region AS region_from,
            T2.region AS region_to,
            T1.waypoint_id AS id_from,
            T2.waypoint_id AS id_to
            FROM
            waypoint T1
            LEFT JOIN
            airway
            ON
            T1.waypoint_id = airway.from_waypoint_id
            LEFT JOIN
            waypoint T2
            ON
            T2.waypoint_id = airway.to_waypoint_id
            WHERE
            (T1.region = 'VD'
            AND
            T2.region = 'VT')
            OR
            (T1.region = 'VL'
            AND
            T2.region = 'VT')
            OR
            (T1.region = 'VV'
            AND
            T2.region = 'VT')
            OR
            (T1.region = 'VY'
            AND
            T2.region = 'VT')
            OR
            (T1.region = 'WM'
            AND
            T2.region = 'VT')
            OR
            (T1.region = 'WS'
            AND
            T2.region = 'VT')
            ORDER BY T1.region ASC
            """)
        f_waypoint = c.fetchall()        

        for f_wpt_item in f_waypoint:
            if len(f_wpt_item[0]) == 5:
                wpt_file.write(f_wpt_item[0]+';'+str(f_wpt_item[3])+';'+str(f_wpt_item[4])+';'+'0;1;\n')
                continue
                
        print('Waypoint created successfully!')
        #close connection with database
        conn.close()

    def import_vor(self):
        #connect to sqlite3 db
        conn = sqlite3.connect('navdata.sqlite')
        #create cursor
        c = conn.cursor()
        #open/create vor file
        vor_file = open("output\\VTBB.vor", "w")

        c.execute("""SELECT ident, frequency, laty, lonx
        FROM vor
        WHERE region = "VT"
        """)

        vor = c.fetchall()
        #write vor
        for vor_item in vor:
            vor_file.write(vor_item[0]+';'+str(format(vor_item[1] / 1000,'.3f'))+';'+str(vor_item[2])+';'+str(vor_item[3])+';\n')
        print('VOR created successfully')
        #close connection with database
        conn.close()

    def import_ils(self):
        #connect to sqlite3 db
        conn = sqlite3.connect('navdata.sqlite')
        #create cursor
        c = conn.cursor()
        #open/create ils file
        ils_file = open("output\\VTBB.ils", "w")

        c.execute("""SELECT ident, frequency, laty, lonx
        FROM ils
        WHERE region = "VT"
        """)

        ils = c.fetchall()

        for ils_item in ils:
            ils_file.write(ils_item[0]+';'+str(format(ils_item[1] / 1000,'.3f'))+';'+str(ils_item[2])+';'+str(ils_item[3])+';\n')
        print('ILS created successfully')
        #close connection with database
        conn.close()

    def impot_ndb(self):
        #connect to sqlite3 db
        conn = sqlite3.connect('navdata.sqlite')
        #create cursor
        c = conn.cursor()
        #open/create ndb file
        ndb_file = open("output\\VTBB.ndb", "w")

        c.execute("""SELECT ident, frequency, laty, lonx
        FROM ndb
        WHERE region = "VT"
        """)

        ndb = c.fetchall()

        for ndb_item in ndb:
            ndb_file.write(ndb_item[0]+';'+str(format(ndb_item[1] / 1000,'.3f'))+';'+str(ndb_item[2])+';'+str(ndb_item[3])+';\n')
        print('NDB created successfully!')
        #close connection with database
        conn.close()
        
    def import_rwy(self):
        #connect to sqlite3 db
        conn = sqlite3.connect('navdata.sqlite')
        #create cursor
        c = conn.cursor()
        #open/create ndb file
        rwy_file = open("output\\VTBB.rwy", "w")

        c.execute("""SELECT
        airport.ident,
        runway_end.name AS runway1,
        runway_end.altitude AS alt1,
        runway_end.heading AS hdg1,
        runway_end.laty AS lat1,
        runway_end.lonx AS lon1
        FROM
        airport
        INNER JOIN
        runway
        INNER JOIN
        runway_end
        WHERE
        airport.region = "VT"
        AND
        runway.airport_id = airport.airport_id
        AND
        runway_end.runway_end_id = primary_end_id
        """)

        runway1 = c.fetchall()

        c.execute("""SELECT
        runway_end.name AS runway2,
        runway_end.altitude AS alt2,
        runway_end.heading AS hdg2,
        runway_end.laty AS lat2,
        runway_end.lonx AS lon2
        FROM
        airport
        INNER JOIN
        runway
        INNER JOIN
        runway_end
        WHERE
        airport.region = "VT"
        AND
        runway.airport_id = airport.airport_id
        AND
        runway_end.runway_end_id = secondary_end_id
        """)

        runway2 = c.fetchall()

        for (run1, run2) in zip(runway1, runway2):
            rwy_file.write(run1[0]+';'+run1[1]+';'+run2[0]+';'+str(run1[2])+';'+str(run2[1])+';'+str(round(run1[3]))+
            ';'+str(round(run2[2]))+';'+str(round(run1[4],10))+';'+str(round(run1[5],9))+';'+str(round(run2[3],10))+
            ';'+str(round(run2[4],9))+';\n')
        print('Runway created successfully')
        #close connection with database
        conn.close()

    def import_airway(self):
        #connect to sqlite3 db
        conn = sqlite3.connect('navdata.sqlite')
        #create cursor
        c = conn.cursor()
        #open/create ndb file
        aiw_file = open("output\\VTBB.aiw", "w")

        c.execute("""
        SELECT
        airway.airway_name AS name,
        airway.airway_fragment_no AS segment_no,
        airway.sequence_no,
        T1.ident as wpt_from,
        T2.ident as wpt_to,
        airway.airway_type AS type,
        airway.from_laty AS from_lat,
        airway.from_lonx AS from_lon,
        airway.to_laty AS to_lat,
        airway.to_lonx AS to_lon,
        airway.direction,
        T1.region AS region_from,
        T2.region AS region_to,
        T1.waypoint_id AS id_from,
        T2.waypoint_id AS id_to
        FROM
        (
            airway
            INNER JOIN
            waypoint T1
            ON
            airway.from_waypoint_id = T1.waypoint_id
            INNER JOIN
            waypoint T2
            ON  
            airway.to_waypoint_id = T2.waypoint_id
        )
        WHERE
        (
            T1.region = 'VT'
            OR
            T2.region = 'VT'
        )
        ORDER BY airway_id ASC;
        """)

        airway = c.fetchall()