
SELECT 
    owner.owner_id, 
    owner.owner_name, 
    COUNT(DISTINCT category.category_id) AS different_category_count 
FROM 
    article 
    JOIN owner ON article.owner_id = owner.owner_id 
    JOIN category_article_mapping ON article.article_id = category_article_mapping.article_id 
    JOIN category ON category_article_mapping.category_id = category.category_id 
GROUP BY 
    owner.owner_id 
ORDER BY 
    different_category_count DESC;
