DROP TABLE if exists authorizer_table;

CREATE TABLE authorizer_table(id SERIAL PRIMARY KEY,name text NOT NULL,password integer NOT NULL);
INSERT INTO authorizer_table(name,password)VALUES('Misa',12345);



DROP TABLE if exists venue_category;

CREATE TABLE venue_category(
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    img_pic VARCHAR(500)
);

INSERT INTO venue_category(name,img_pic)
VALUES
('Waterfront','https://www.costadeste.com/i/SITE_161213_12163014_WNF14/content/CMS_12132016_124202487_EC52W/7648B862-9116-4637-37AA4F82F3956B14.JPG'),
('Winery','https://crowneplazahuntervalley.com.au/wp-content/uploads/2022/01/4.png'),
('City','https://www.theparkmelbourne.com.au/wp-content/uploads/2018/08/Image-4.jpg'),
('Historic','https://weddingvenuemap.com/wp-content/uploads/2021/10/69_the-howey-mansion6a853ba32c2c6a632013628bb7a918ef-scaled.jpeg'),
('Unique','https://img.sunset02.com/sites/default/files/styles/4_3_horizontal_inbody_900x506/public/image/2017/05/main/cornerstone-venue_0.jpg');




DROP TABLE if exists winery_list_table;

CREATE TABLE winery_list_table(
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    img_pic TEXT NOT NULL,
    location TEXT NOT NULL,
    overview TEXT NULL,
    avg_price integer NULL,
    avg_ppl integer NULL
);

INSERT INTO winery_list_table(name,img_pic,location,overview,avg_price,avg_ppl)
VALUES
('Stones of the Yarra Valley','https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQoz19xb1QvAtolQmUCOt5sOBQRj0JCnOkPFg&usqp=CAU','Coldstream','text',40000,200),
('Zonzo','https://www.rosaphoto.com.au/wp-content/uploads/2022/07/Zonzo-Estate-Yarra-Valley-wedding-photos-Zonzo-Estate-Yarra-Valley-receptions-wedding-photographer-photography-0055.jpg','Yarra Glen','text',30000,130),
('Immerse','https://blackavenueproductions.com.au/wp-content/uploads/2018/03/rustic-wedding-at-Immerse-Yarra-Valley-photo.jpg','Dixons Creek','text',25000,100),
('ACACIA RIDGE','https://www.michaelbriggs.com.au/wp-content/uploads/2020/06/yarra-valley-wedding-venue-with-marquee_0001.jpg','Yarra Glen','text',32000,120),
('coombe','https://i.pinimg.com/736x/46/48/47/4648470e9549ab4ccbd98a0d37490b02--wedding-events-wedding-reception.jpg','Coldstream','text',25000,150);


DROP TABLE if exists city_venue_list_table;

CREATE TABLE city_venue_list_table(
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    img_pic TEXT NOT NULL,
    location TEXT NOT NULL,
    overview TEXT NULL,
    avg_price integer NULL,
    avg_ppl integer NULL
);

INSERT INTO city_venue_list_table(name,img_pic,location,overview,avg_price,avg_ppl)
VALUES
('Metoroplis','https://www.metropolisevents.com.au/wp-content/uploads/2021/12/HR_NatalieandAnthony_Metropolis_LostinlovePhotography860-2.jpg','CBD','When it comes to venues that exude luxury and high-end glamour, Metropolis Events in Southbank is inferior to none. Boasting unparalleled views of the Melbourne city skyline, this New York loft-style venue has a flexible layout that is perfect for grand weddings. With a capacity for up to 1100 standing guests and 402 for seated dining, Metropolis Events is ideal for both ceremonies and receptions.',50000,200),
('Crown Melbourne','https://weddingsofdistinction.com.au/wp-content/uploads/2022/04/190826-Crown-Melbourne-Weddings-Venues-River-Room.jpg','CBD','text',50000,250),
('Leonda by the yarra','https://ateiaphotography.com.au/wp-content/uploads/2021/08/ATEIA-Photography-Video-Wedding-Photography-Melbourne-www.ATEIAphotography.com_.au-20-of-20.jpg','Howthorn','text',30000,250),
('Luminare','https://www.hiddencitysecrets.com.au/wp-content/uploads/2017/06/Luminare-Unique-Venue-Hire-South-Melbourne-Function-Rooms-Venues-Party-Birthday-Wedding-Corporate-Cocktail-Outdoor-Product-Launch-Engagement-Amazing-Private-Dining-Event-003.jpg','South Melbourne','text',40000,180),
('Vue de Monde','https://images-cdn.easyweddings.com.au/s3/prod-ew-image-global-v2/Live/ImageUploader/-supplierprofilelive-photo-726bee8a-2ede-4644-8ad7-c38012e1675e.jpg?quality=80&format=jpg&mode=crop&autorotate=true&crop=0,0,0,0&width=2048','CBD','TEXT',30000,60),
('Park Hyatt Melbourne','https://images.squarespace-cdn.com/content/v1/5b99e43936099b7e59494482/1538016381053-6JDRZSLCKR5QRUY34H2W/180120-Park%2520Hyatt%25202_162819_8914_preview.jpeg.jpg?format=1000w','CBD','text',60000,150);