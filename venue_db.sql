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



DROP TABLE if exists waterfront_list_table;

CREATE TABLE waterfront_list_table(
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    img_pic TEXT NOT NULL,
    location TEXT NOT NULL,
    overview TEXT NULL,
    avg_price integer NULL,
    avg_ppl integer NULL
);

INSERT INTO waterfront_list_table(name,img_pic,location,overview,avg_price,avg_ppl)
VALUES
('Carousel','https://simplycelebrant.com.au/wp-content/uploads/2020/05/carousel-Food-Desire-462x310.jpg','Albert Park','TEXt.',4000,180),
('The Portsea Hotel','https://images-cdn.easyweddings.com.au/s3/prod-ew-image-global-v2/release/ImageUploader/Port-Sea-Hotel-2086-P1660065-1930120400.jpg?quality=80&format=jpg&mode=crop&autorotate=true&crop=0,0,0,0&width=2048','Portsea','text',30000,80),
('Sandringham Yacht Club','https://simplycelebrant.com.au/wp-content/uploads/2018/07/SYC.jpg','Sandringham','text',35000,200),
('Port Melbourne Yacht Club','https://atlanticgroup.com.au/wp-content/uploads/2019/02/Port-Melb-Yacht-Club-Preview-Pic.jpg','Port Melbourne','text',20000,180),
('encore St kilda beach','https://inphotography.com.au//wp-content/uploads/2015/12/in-photography.MichellePragt1.jpg','St Kilda','TEXT',25000,100);




DROP TABLE if exists historic_list_table;

CREATE TABLE historic_list_table(
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    img_pic TEXT NOT NULL,
    location TEXT NOT NULL,
    overview TEXT NULL,
    avg_price integer NULL,
    avg_ppl integer NULL
);
INSERT INTO historic_list_table(name,img_pic,location,overview,avg_price,avg_ppl)
VALUES
('The George Ballroom','https://assets.venuecrew.com/wp-content/uploads/2023/01/12051747/ChloeandBenPreviews-40.jpg','st Kilda','TEXt.',35000,120),
('Werribee Mansion','https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR-VErarZVoApBQhNBnyc3GSidK8KWjyGvsbvG-cTRIji3d9hVV5ps5Pq7TrYBQWZtQ1fo&usqp=CAU','Werribee','text',40000,80),
('Panama Dining Room','https://images.squarespace-cdn.com/content/v1/557aa90fe4b05469e3abc859/1682214610625-HCFI38DXENDWCOKJ2PT5/Long-Way-Home_Clare-Blake_sneak-peek-27.jpg?format=2500w','Fizroy','text',20000,80),
('Ripponlea','https://www.nationaltrust.org.au/wp-content/uploads/2015/09/MadelineKate_EJ-0510-783x522.jpg','Ripponlea','text',30000,180),
('Quat quat','https://images.squarespace-cdn.com/content/v1/58e35aba6b8f5bb18b0d2944/1567659669092-X8W1315WU3QX5QX6S7B5/Quat+Quatta+Styling.jpg','Ripponlea','TEXT',25000,70),
('Monstalvat','https://static.showit.co/1200/d7DbM8uaQui5jdgjjgIgLw/109919/montsalvat00108.jpg','Eltham','text',38000,90);




DROP TABLE if exists unique_list_table;
CREATE TABLE unique_list_table(
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    img_pic TEXT NOT NULL,
    location TEXT NOT NULL,
    overview TEXT NULL,
    avg_price integer NULL,
    avg_ppl integer NULL
);
INSERT INTO unique_list_table(name,img_pic,location,overview,avg_price,avg_ppl)
VALUES
('Melbourne ZOO','https://www.melbournezooevents.com.au/wp-content/uploads/KMHRCOL-766-1024x683.jpg','Parkvill','TEXt.',25000,100),
('Sea Life Aquarium','https://cdn-goimh.nitrocdn.com/LyAXmKQzbBhSkvAJleRLJoQdWcloLhAR/assets/images/optimized/rev-ee8eeae/wp-content/uploads/2019/03/SEA_LIFE_Melbourne_Aquarium.jpg','CBD','text',50000,300),
('State Library','https://partyspace.com/images/providers/Peabody%20Library%20wedding%20venue.jpg','CBD','text',60000,250),
('Melbourne Museum ','https://cdn0.weddingwire.com/vendor/710496/3_2/960/jpg/15eb31aba5b0eb5509ea0e3e229bc1fb_51_694017-161298520566752.jpeg','Carlton','text',30000,150),
('Gather&Tailor','https://briarsatlas.com/wp-content/uploads/2020/07/Gather-And-Tailor-Wedding-9417.jpg','West Melbourne','TEXT',20000,200),
('Botanical Garden','https://www.blakesfeast.com.au/wp-content/uploads/J00667-0680.jpg','Melbourne','text',50000,300),
('Glasshaus','https://i.weddinghero.com.au/gallery/1675/preview_1675_hIjQqzTL.jpg','Richmond','TEXT',20000,70);





-- DROP TABLE if exists users;
-- CREATE TABLE users(
--     id SERIAL PRIMARY KEY,
--     email TEXT NOT NULL,
--     name VARCHAR(50) NOT NULL,
--     password_hash TEXT NOT NULL
-- );
-- INSERT INTO users(email,name,password_hash)
-- VALUES
-- -- ('eee@gmail.com','hello','123A'),
-- -- ('zzz@test.com','world','123B'),
-- -- ('hhh@test.com','check','123C');
-- ('foo@gmail.com', 'foo bar', '$2b$12$l4i64Xk9Iy7kZktddKlqHOoq4U80lphevF5IPsGcI3eFmZz55GGTe'),
-- ('bar@hotmail.com', 'bar baz', '$2b$12$l4i64Xk9Iy7kZktddKlqHO05wtZUyMhEO1z3OiVOd9/Tb5oBTkW3S');



DROP TABLE if exists users;
CREATE TABLE users(
    id SERIAL PRIMARY KEY,
    email TEXT NOT NULL,
    name VARCHAR(50) NOT NULL,
    weddingDate text,
    guestNum integer,
    budget integer,
    password_hash TEXT NOT NULL
);
INSERT INTO users(email,name,weddingDate,guestNum,budget,password_hash)
VALUES
('eee@gmail.com','hello','November',250,70000,'$2b$12$x3uLjkZd3xuBJmhbOzFbmeUXmnB5AG6xFEkkiDw5LpR4utmjobL/e'),
('zzz@test.com','world','December',150,50000,'123BfasfvsDFW'),
('hhh@test.com','check','May',50,15000,'123CwFAWSVAS');
