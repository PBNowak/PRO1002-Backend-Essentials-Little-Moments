
-- Sample tags for Little Moments

INSERT INTO tags (name) VALUES
('Nature'),
('Slow Living'),
('Everyday Life'),
('Mindfulness'),
('Seasons');


-- Sample blog posts for Little Moments

INSERT INTO posts (title, body, published_date) VALUES
('A Quiet Morning in the Woods',
'There is something peaceful about walking through the woods early in the morning. The air feels fresh, the birds are singing, and everything seems to slow down. It is a simple reminder to enjoy the little moments around us.',
'2026-10-20'),

('The Beauty of Slow Living',
'Life can become busy, and sometimes we forget to enjoy the present moment. Slow living is about making time for things that matter, appreciating small experiences, and finding a comfortable balance in everyday life.',
'2026-10-18'),

('Finding Joy in Small Things',
'Happiness does not always come from big achievements. Sometimes it is a warm cup of tea, a beautiful sunset, or a quiet afternoon at home. Learning to appreciate these moments can make ordinary days feel special.',
'2026-10-15'),

('Why I Love Autumn',
'Autumn brings beautiful colours, cooler mornings, and a feeling of calm. Walking among fallen leaves and watching nature change is one of my favourite parts of the season. It is a perfect time to slow down and enjoy being outside.',
'2026-10-12'),

('A Walk Without a Destination',
'Not every walk needs a plan. Sometimes it is nice to simply leave the house and see where the path leads. Walking without a destination gives me time to think, relax, and notice things I would normally miss.',
'2026-10-09'),

('Creating a Cozy Home',
'A cozy home does not need expensive decorations. Soft blankets, warm lighting, natural materials, and a few personal touches can make a space feel welcoming. For me, comfort is more important than perfection.',
'2026-10-06'),

('Learning to Appreciate Rainy Days',
'Rainy days are often seen as something negative, but they can be peaceful too. The sound of rain against the window, a good book, and a warm drink can turn a grey afternoon into something enjoyable.',
'2026-10-03'),

('The Simple Pleasure of Gardening',
'Gardening is a wonderful way to connect with nature. Watching plants grow teaches patience and reminds us that good things take time. Even a few flowers or herbs can bring happiness to everyday life.',
'2026-09-29'),

('Taking a Break from Screens',
'Technology is useful, but sometimes it is important to disconnect. Spending time outdoors, reading, or doing something creative can help clear the mind. Small breaks from screens can make a big difference.',
'2026-09-25'),

('Finding Balance in Everyday Life',
'Balancing responsibilities, work, and personal time is not always easy. I am learning that balance does not mean doing everything perfectly. Sometimes it simply means knowing when to slow down and take a break.',
'2026-09-20');


-- Connect blog posts to their tags

INSERT INTO post_tags (post_id, tag_id) VALUES
(1, 1), (1, 4),
(2, 2), (2, 4),
(3, 3), (3, 4),
(4, 1), (4, 5),
(5, 1), (5, 2),
(6, 2), (6, 3),
(7, 2), (7, 5),
(8, 1), (8, 3),
(9, 3), (9, 4),
(10, 2), (10, 3);
