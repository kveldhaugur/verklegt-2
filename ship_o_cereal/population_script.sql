INSERT INTO main_manufacturer (ManID, NAME)
VALUES
    ( 1,  'General Mills'),
    ( 2,  'Nabisco'),
    ( 3,  'Kellogg''s'),
    ( 4,  'Ralston'),
    ( 5,  'Nestle'),
    ( 6,  'Quaker'),
    ( 7,  'Post Cereal');

INSERT INTO main_items (ItemID, Image, Quantity, Price, Name, Description, ManID)
VALUES
(1 , 'Travis_scott_reeses_puffs.jpg', 1, 'Travis scott Reeses', 100, 'This limited brand was sold in 2019, a super limited brand designed by the rapper, Travis Scott, himself'),
(2 , 'Reeses_norm.png', 1, 'Reeses puffs', 10, 'This strictly worse brand from it''s much more limited counterpart, designed by Travis Scott still somehow manages to sell despite it''s lack of superiority. We don''t know how.'),
(3 , 'Lucky_Charms.jpg', 1, 'Lucky Charms', 15, 'The ultimate in ultimate cereal to start your day. Do it the right way with Lucky Charms™'),
(4 , 'Cheerios_ice.jpg', 1, 'Cheerios', 8, 'A very popular, tasteless "thing". We have no idea why it''s so popular'),
(5 , 'Chips_ahoy.jpg', 2, 'Chips Ahoy', 13, 'This miniature cookie based brand fools you into thinking it''s healthy because it''s marketed as a breakfast. But who''s to judge when you get to eat cookies at 7am'),
(6 , 'Coco_pops.jpg', 3, 'Coco Pops', 15, 'There''s a monkey on the cover!'),
(7 , 'Dunkin_caramel.jpg', 4, 'Dunkin Donuts cereal', 25, 'There might be some illegal compunds in here, but we won''t tell if you won''t'),
(8 , 'Pac_man.jpg', 1, 'Pac-Man cereal', 120, 'One of the best ways to start the day! A blast from the past! Get your nostalgia here folks!'),
(9 , 'C3P0s.jpg', 3, 'C-3PO''s cereal', 200, 'This cencturies old robotic nerd from a galaxy far, far away invades our reality by forcing a healthy product depicting his supremacy, we were threatened against our will to sell his product or face certain human extinction'),
(10 , 'Waffleos.jpg', 4, 'Waffelos', 20, 'Isn''t this the dude from that cartoon?'),
(11 , 'Buc_Wheats.jpg', 1, 'Buc Wheats', 1, 'This old product from the ancient 70''s, still hasn''t changed in flavour or quality (as if there was any to begin with). It has stayed on shelf for 50 years and it doesnt matter how big of a discount we offer, they will never sell'),
(12 , 'Mr_ts.jpg', 6, 'MR.T cereal', 200, 'I pity da foo'' who don'' eat my cereal!'),
(13 , 'Croonchy_stars.jpg', 7, 'Croonchy stars', 120, 'The swedish chef has done it again, an absolute delicacy of cinnamonny delight'),
(14 , 'ETs.jpg', 1, 'E.T. Cereal', 200, 'Food only produced for alien lifeforms, searching for a phone'),
(15 , 'Smurf_berry_crunch.jpg', 7, 'Smurf Berry Crunch', 20, 'A red cereal for blue people. What has the world come to?'),
(16 , 'Oreos.jpg', 7, 'Oreo O''s cereal', 15, 'Some people can''t get enough of the cream sandwich, So they made them small enough for a bowl'),
(17 , 'Fruit_Loops.jpg', 3, 'Fruit Loops', 15, 'Cheerios, but with actual flavour, done inadequately... They smell kinda funny'),
(18 , 'Honey_nut.jpg', 1, 'Honey Nut Cheerios', 15, 'Cheerios, but with actual flavour, This time done right but with a stupidly irritating bumblebee. Save the bees!'),
(19 , 'Rice_krispies.jgp', 3, 'Rice Krispies', 10, 'Coco puffs for white people. Nobody eats these raw, they only exists as an ingredient to a treat'),
(20 , 'Capn_crunch.jgp', 6, 'Captain Crunch', 14, 'Is he really a captain? Has anyone seen his ship?'),
(21 , 'Frosties.jgp', 3, 'Frosted Flakes', 15, 'After Tony got assaulted on Twitter by evil furries, he needs your help to recover from his mental abuse, we have a special offer of 2 for 1 during his time of need'),
(22 , 'nothing for now', 5, 'Water from mars', 450, 'For rich people who dont eat'),
(23 , 'nothing for now', 5, 'Dirty water', 50, 'For poor people'),
(24 , 'nothing for now', 3, 'Used bath water', '200, Straight from Tony''s bathtub, this special offer grants you a lifetime opportunity to have a permanent reminiscence of everybody''s favorite anthromorphised mascot... Or you can just drink it if you''re that degenerate'),
(25 , 'Dont_talk_to_me.png', 3, 'Don''t Talk To Me Mug', 50, 'Sometimes you just really gotta have your frosties before making any social contact'),
(26 , 'Live_laugh_lucky.png', 1, 'Live, Laugh, Lucky Charms Painting', 50, 'A high quality painting aggressively ordering anecdotal lifestyles upon any who grace eyes upon it')

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
(22, 'Painting')

INSERT INTO main_items_Tags (items_id, itemcategory_id)
VALUES
(1 , 1),
(1 , 2),
(1 , 3),
(1 , 4),
(1 , 5),
(1 , 6),
(1 , 7),
(2 , 1),
(2 , 2),
(2 , 3),
(2 , 5),
(2 , 6),
(3 , 8),
(3 , 2),
(3 , 6),
(4 , 9),
(4 , 10),
(4 , 11),
(4 , 6),
(5 , 6),
(5 , 3),
(5 , 2),
(5 , 12),
(5 , 13),
(6 , 6),
(6 , 2),
(6 , 3),
(7 , 6),
(7 , 2),
(7 , 3),
(8 , 2),
(8 , 5),
(8 , 8),
(8 , 6),
(9 , 6),
(9 , 7),
(9 , 10),
(9 , 11),
(10 , 14),
(10 , 2),
(10 , 12),
(10 , 6),
(11 , 6),
(11 , 15),
(11 , 13),
(11 , 10),
(12 , 6),
(12 , 7),
(12 , 10),
(12 , 11),
(13 , 6),
(13 , 16),
(14 , 6),
(14 , 7),
(15 , 6),
(15 , 7),
(15 , 10),
(15 , 11),
(15 , 2),
(16 , 6),
(16 , 3),
(16 , 5),
(17 , 6),
(17 , 11),
(17 , 2),
(17 , 17),
(18 , 6),
(18 , 2),
(19 , 6),
(19 , 11),
(19 , 10),
(20 , 2),
(20 , 5),
(20 , 6),
(21 , 2),
(21 , 6),
(21 , 13),
(22 , 18),
(22 , 19),
(22 , 9),
(22 , 20),
(22 , 10),
(23 , 9),
(23 , 10),
(23 , 12),
(23 , 20),
(24 , 20),
(24 , 13),
(24 , 7),
(25 , 20),
(25 , 21),
(26 , 20),
(26 , 22);

INSERT INTO main_country VALUES
(1, 'Afghanistan')
(2,	'Aland Islands'),
(3,	'Albania'),
(4,	'Algeria'),
(5,	'American Samoa'),
(6,	'Andorra'),
(7,	'Angola'),
(8,	'Anguilla'),
(9,	'Antarctica'),
(10, 'Antigua and Barbuda'),
(11, 'Argentina'),
(12, 'Armenia'),
(13, 'Aruba'),
(14, 'Australia'),
(15, 'Austria'),
(16, 'Azerbaijan'),
(17, 'Bahamas'),
(18, 'Bahrain'),
(19, 'Bangladesh'),
(20, 'Barbados'),
(21, 'Belarus'),
(22, 'Belgium'),
(23, 'Belize'),
(24, 'Benin'),
(25, 'Bermuda'),
(26, 'Bhutan'),
(27, 'Bolivia'),
(28, 'Bonaire, Sint Eustatius and Saba'),
(29, 'Bosnia and Herzegovina'),
(30, 'Botswana'),
(31, 'Bouvet Island'),
(32, 'Brazil'),
(33, 'British Indian Ocean Territory'),
(34, 'Brunei'),
(35, 'Bulgaria'),
(36, 'Burkina Faso'),
(37, 'Burundi'),
(38, 'Cambodia'),
(39, 'Cameroon'),
(40, 'Canada'),
(41, 'Cape Verde'),
(42, 'Cayman Islands'),
(43, 'Central African Republic'),
(44, 'Chad'),
(45, 'Chile'),
(46, 'China'),
(47, 'Christmas Island'),
(48, 'Cocos (Keeling) Islands'),
(49, 'Colombia'),
(50, 'Comoros'),
(51, 'Congo'),
(52, 'Cook Islands'),
(53, 'Costa Rica'),
(54, 'Ivory Coast'),
(55, 'Croatia'),
(56, 'Cuba'),
(57, 'Curacao'),
(58, 'Cyprus'),
(59, 'Czech Republic'),
(60, 'Democratic Republic of the Congo'),
(61, 'Denmark'),
(62, 'Djibouti'),
(63, 'Dominica'),
(64, 'Dominican Republic'),
(65, 'Ecuador'),
(66, 'Egypt'),
(67, 'El Salvador'),
(68, 'Equatorial Guinea'),
(69, 'Eritrea'),
(70, 'Estonia'),
(71, 'Ethiopia'),
(72, 'Falkland Islands (Malvinas)'),
(73, 'Faroe Islands'),
(74, 'Fiji'),
(75, 'Finland'),
(76, 'France'),
(77, 'French Guiana'),
(78, 'French Polynesia'),
(79, 'French Southern Territories'),
(80, 'Gabon'),
(81, 'Gambia'),
(82, 'Georgia'),
(83, 'Germany'),
(84, 'Ghana'),
(85, 'Gibraltar'),
(86, 'Greece'),
(87, 'Greenland'),
(88, 'Grenada'),
(89, 'Guadaloupe'),
(90, 'Guam'),
(91, 'Guatemala'),
(92, 'Guernsey'),
(93, 'Guinea'),
(94, 'Guinea-Bissau'),
(95, 'Guyana'),
(96, 'Haiti'),
(97, 'Heard Island and McDonald Islands'),
(98, 'Honduras'),
(99, 'Hong Kong'),
(100, 'Hungary'),
(101, 'Iceland'),
(102, 'India'),
(103, 'Indonesia'),
(104, 'Iran'),
(105, 'Iraq'),
(106, 'Ireland'),
(107, 'Isle of Man'),
(108, 'Israel'),
(109, 'Italy'),
(110, 'Jamaica'),
(111, 'Japan'),
(112, 'Jersey'),
(113, 'Jordan'),
(114, 'Kazakhstan'),
(115, 'Kenya'),
(116, 'Kiribati'),
(117, 'Kosovo'),
(118, 'Kuwait'),
(119, 'Kyrgyzstan'),
(120, 'Laos'),
(121, 'Latvia'),
(122, 'Lebanon'),
(123, 'Lesotho'),
(124, 'Liberia'),
(125, 'Libya'),
(126, 'Liechtenstein'),
(127, 'Lithuania'),
(128, 'Luxembourg'),
(129, 'Macao'),
(130, 'Macedonia'),
(131, 'Madagascar'),
(132, 'Malawi'),
(133, 'Malaysia'),
(134, 'Maldives'),
(135, 'Mali'),
(136, 'Malta'),
(137, 'Marshall Islands'),
(138, 'Martinique'),
(139, 'Mauritania'),
(140, 'Mauritius'),
(141, 'Mayotte'),
(142, 'Mexico'),
(143, 'Micronesia'),
(144, 'Moldava'),
(145, 'Monaco'),
(146, 'Mongolia'),
(147, 'Montenegro'),
(148, 'Montserrat'),
(149, 'Morocco'),
(150, 'Mozambique'),
(151, 'Myanmar (Burma)'),
(152, 'Namibia'),
(153, 'Nauru'),
(154, 'Nepal'),
(155, 'Netherlands'),
(156, 'New Caledonia'),
(157, 'New Zealand'),
(158, 'Nicaragua'),
(159, 'Niger'),
(160, 'Nigeria'),
(161, 'Niue'),
(162, 'Norfolk Island'),
(163, 'North Korea'),
(164, 'Northern Mariana Islands'),
(165, 'Norway'),
(166, 'Oman'),
(167, 'Pakistan'),
(168, 'Palau'),
(169, 'Palestine'),
(170, 'Panama'),
(171, 'Papua New Guinea'),
(172, 'Paraguay'),
(173, 'Peru'),
(174, 'Phillipines'),
(175, 'Pitcairn'),
(176, 'Poland'),
(177, 'Portugal'),
(178, 'Puerto Rico'),
(179, 'Qatar'),
(180, 'Reunion'),
(181, 'Romania'),
(182, 'Russia'),
(183, 'Rwanda'),
(184, 'Saint Barthelemy'),
(185, 'Saint Helena'),
(186, 'Saint Kitts and Nevis'),
(187, 'Saint Lucia'),
(188, 'Saint Martin'),
(189, 'Saint Pierre and Miquelon'),
(190, 'Saint Vincent and the Grenadines'),
(191, 'Samoa'),
(192, 'San Marino'),
(193, 'Sao Tome and Principe'),
(194, 'Saudi Arabia'),
(195, 'Senegal'),
(196, 'Serbia'),
(197, 'Seychelles'),
(198, 'Sierra Leone'),
(199, 'Singapore'),
(200, 'Sint Maarten'),
(201, 'Slovakia'),
(202, 'Slovenia'),
(203, 'Solomon Islands'),
(204, 'Somalia'),
(205, 'South Africa'),
(206, 'South Georgia and the South Sandwich '),
(207, 'South Korea'),
(208, 'South Sudan'),
(209, 'Spain'),
(210, 'Sri Lanka'),
(211, 'Sudan'),
(212, 'Suriname'),
(213, 'Svalbard and Jan Mayen'),
(214, 'Swaziland'),
(215, 'Sweden'),
(216, 'Switzerland'),
(217, 'Syria'),
(218, 'Taiwan'),
(219, 'Tajikistan'),
(220, 'Tanzania'),
(221, 'Thailand'),
(222, 'Timor-Leste (East Timor)'),
(223, 'Togo'),
(224, 'Tokelau'),
(225, 'Tonga'),
(226, 'Trinidad and Tobago'),
(227, 'Tunisia'),
(228, 'Turkey'),
(229, 'Turkmenistan'),
(230, 'Turks and Caicos Islands'),
(231, 'Tuvalu'),
(232, 'Uganda'),
(233, 'Ukraine'),
(234, 'United Arab Emirates'),
(235, 'United Kingdom'),
(236, 'United States'),
(237, 'United States Minor Outlying Islands'),
(238, 'Uruguay'),
(239, 'Uzbekistan'),
(240, 'Vanuatu'),
(241, 'Vatican City'),
(242, 'Venezuela'),
(243, 'Vietnam'),
(244, 'Virgin Islands, British'),
(245, 'Virgin Islands, US'),
(246, 'Wallis and Futuna'),
(247, 'Western Sahara'),
(248, 'Yemen'),
(249, 'Zambia'),
(250, 'Zimbabwe');
