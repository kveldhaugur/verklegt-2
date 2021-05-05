INSERT INTO main_manufacturer (ManID, NAME)
VALUES
    ( 1,  'General Mills'),
    ( 2,  'Nabisco'),
    ( 3,  'Kellogg''s'),
    ( 4,  'Ralston'),
    ( 5,  'Nestle'),
    ( 6,  'Quaker'),
    ( 7,  'Post Cereal');

INSERT INTO main_items (ItemID, ManID, Quantity, Price, Name, Description, Image)
VALUES
        (1, 1, 10, 100, 'Travis scott Reeses',
        'This limited brand was sold in 2019, a super limited brand designed by the rapper, Travis Scott, himself',
        'Travis_scott_reeses_puffs.jpg'),
       (2, 1, 10, 10, 'Reeses puffs',
        'This strictly worse brand from it''s much more limited counterpart, designed by Travis Scott still somehow manages to sell despite it''s lack of superiority. We don''t know how.',
        'Reeses_norm.png'),
       (3, 1, 10, 15, 'Lucky Charms',
        'The ultimate in ultimate cereal to start your day. Do it the right way with Lucky Charms™',
        'Lucky_Charms.jpg'),
       (4, 1, 10, 8, 'Cheerios', 'A very popular, tasteless "thing". We have no idea why it''s so popular',
        'Cheerios_ice.jpg'),
       (5,  2,10, 13, 'Chips Ahoy',
        'This miniature cookie based brand fools you into thinking it''s healthy because it''s marketed as a breakfast. But who''s to judge when you get to eat cookies at 7am',
        'Chips_ahoy.jpg'),
       (6, 3, 10, 15, 'Coco Pops', 'There''s a monkey on the cover!', 'Coco_pops.jpg'),
       (7, 4, 10, 25, 'Dunkin Donuts cereal',
        'There might be some illegal compunds in here, but we won''t tell if you won''t', 'Dunkin_caramel.jpg'),
       (8, 1, 10, 120, 'Pac-Man cereal',
        'One of the best ways to start the day! A blast from the past! Get your nostalgia here folks!', 'Pac_man.jpg'),
       (9, 3, 10, 200, 'C-3PO''s cereal',
        'This cencturies old robotic nerd from a galaxy far, far away invades our reality by forcing a healthy product depicting his supremacy, we were threatened against our will to sell his product or face certain human extinction',
        'C3P0s.jpg'),
       (10, 4, 10, 20, 'Waffelos', 'Isn''t this the dude from that cartoon?', 'Waffleos.jpg'),
       (11, 1, 10, 1, 'Buc Wheats',
        'This old product from the ancient 70''s, still hasn''t changed in flavour or quality (as if there was any to begin with). It has stayed on shelf for 50 years and it doesnt matter how big of a discount we offer, they will never sell',
        'Buc_Wheats.jpg'),
       (12, 6, 10, 200, 'MR.T cereal', 'I pity da foo'' who don'' eat my cereal!', 'Mr_ts.jpg'),
       (13, 7, 10, 120, 'Croonchy stars',
        'The swedish chef has done it again, an absolute delicacy of cinnamonny delight', 'Croonchy_stars.jpg'),
       (14, 1, 10, 200, 'E.T. Cereal', 'Food only produced for alien lifeforms, searching for a phone', 'ETs.jpg'),
       (15, 7, 10, 20, 'Smurf Berry Crunch', 'A red cereal for blue people. What has the world come to?',
        'Smurf_berry_crunch.jpg'),
       (16, 7, 10, 15, 'Oreo O''s cereal',
        'Some people can''t get enough of the cream sandwich, So they made them small enough for a bowl', 'Oreos.jpg'),
       (17, 3, 10, 15, 'Fruit Loops', 'Cheerios, but with actual flavour, done inadequately... They smell kinda funny',
        'Fruit_Loops.jpg'),
       (18, 1, 10, 15, 'Honey Nut Cheerios',
        'Cheerios, but with actual flavour, This time done right but with a stupidly irritating bumblebee. Save the bees!',
        'Honey_nut.jpg'),
       (19, 3, 10, 10, 'Rice Krispies',
        'Coco puffs for white people. Nobody eats these raw, they only exists as an ingredient to a treat',
        'Rice_krispies.jgp'),
       (20, 6, 10, 14, 'Captain Crunch', 'Is he really a captain? Has anyone seen his ship?', 'Capn_crunch.jgp'),
       (21, 3, 10, 15, 'Frosted Flakes',
        'After Tony got assaulted on Twitter by evil furries, he needs your help to recover from his mental abuse, we have a special offer of 2 for 1 during his time of need',
        'Frosties.jgp'),
       (22, 5, 10, 450, 'Water from mars', 'For rich people who dont eat', 'nothing for now'),
       (23, 5, 10, 50, 'Dirty water', 'For poor people', 'nothing for now'),
       (24, 3, 10, 200, 'Used bath water',
        'Straight from Tony''s bathtub, this special offer grants you a lifetime opportunity to have a permanent reminiscence of everybody''s favorite anthromorphised mascot... Or you can just drink it if you''re that degenerate',
        'nothing for now'),
       (25, 3, 10, 50, 'Don''t Talk To Me Mug',
        'Sometimes you just really gotta have your frosties before making any social contact', 'Dont_talk_to_me.png'),
       (26, 1, 10, 50, 'Live, Laugh, Lucky Charms Painting',
        'A high quality painting aggressively ordering anecdotal lifestyles upon any who grace eyes upon it',
        'Live_laugh_lucky.png');
INSERT INTO main_itemcategory (CategoryID, CategoryTag)
VALUES
(1, 'Peanuts'),
(2, 'Sugary'),
(3, 'Chocolate'),
(4, 'Superior'),
(5, 'Puffs'),
(6, 'Cereal'),
(7, 'Collector''s item'),
(8, 'Marshmallows'),
(9, 'Healthy'),
(10, 'Keto'),
(11, 'Diet'),
(12, 'Chunky'),
(13, 'Flaky'),
(14, 'Maple'),
(15, 'Nutritious'),
(16, 'Cinnamon'),
(17, 'Fruity'),
(18, 'Low carb'),
(19, 'Low sugar'),
(20, 'Merch'),
(21, 'Mug'),
(22, 'Painting');

INSERT INTO main_items_Tags (items_id, itemcategory_id)
VALUES
INSERT INTO "main_items_Tags"
VALUES (1 , 1, 1),
       (2 , 1, 2),
       (3 , 1, 3),
       (4 , 1, 4),
       (5 , 1, 5),
       (6 , 1, 6),
       (7 , 1, 7),
       (8 , 2, 1),
       (9 , 2, 2),
       (10 , 2, 3),
       (11 , 2, 5),
       (12 , 2, 6),
       (13 , 3, 8),
       (14 , 3, 2),
       (15 , 3, 6),
       (16 , 4, 9),
       (17 , 4, 10),
       (18 , 4, 11),
       (19 , 4, 6),
       (20 , 5, 6),
       (21 , 5, 3),
       (22 , 5, 2),
       (23 , 5, 12),
       (24 , 5, 13),
       (25 , 6, 6),
       (26 , 6, 2),
       (27 , 6, 3),
       (28 , 7, 6),
       (29 , 7, 2),
       (30 , 7, 3),
       (31 , 8, 2),
       (32 , 8, 5),
       (33 , 8, 8),
       (34 , 8, 6),
       (35 , 9, 6),
       (36 , 9, 7),
       (37 , 9, 10),
       (38 , 9, 11),
       (39 , 10, 14),
       (40 , 10, 2),
       (41 , 10, 12),
       (42 , 10, 6),
       (43 , 11, 6),
       (44 , 11, 15),
       (45 , 11, 13),
       (46 , 11, 10),
       (47 , 12, 6),
       (48 , 12, 7),
       (49 , 12, 10),
       (50 , 12, 11),
       (51 , 13, 6),
       (52 , 13, 16),
       (53 , 14, 6),
       (54 , 14, 7),
       (55 , 15, 6),
       (56 , 15, 7),
       (57 , 15, 10),
       (58 , 15, 11),
       (59 , 15, 2),
       (60 , 16, 6),
       (61 , 16, 3),
       (62 , 16, 5),
       (63 , 17, 6),
       (64 , 17, 11),
       (65 , 17, 2),
       (66 , 17, 17),
       (67 , 18, 6),
       (68 , 18, 2),
       (69 , 19, 6),
       (70 , 19, 11),
       (71 , 19, 10),
       (72 , 20, 2),
       (73 , 20, 5),
       (74 , 20, 6),
       (75 , 21, 2),
       (76 , 21, 6),
       (77 , 21, 13),
       (78 , 22, 18),
       (79 , 22, 19),
       (80 , 22, 9),
       (81 , 22, 20),
       (82 , 22, 10),
       (83 , 23, 9),
       (84 , 23, 10),
       (85 , 23, 12),
       (86 , 23, 20),
       (87 , 24, 20),
       (88 , 24, 13),
       (89 , 24, 7),
       (90 , 25, 20),
       (91 , 25, 21),
       (92 , 26, 20),
       (93 , 26, 22);