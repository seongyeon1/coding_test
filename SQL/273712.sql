SELECT ITEM_ID,	ITEM_NAME,	RARITY
FROM  ITEM_INFO
WHERE ITEM_ID NOT IN (SELECT DISTINCT PARENT_ITEM_ID
                     FROM ITEM_TREE
                     WHERE PARENT_ITEM_ID IS NOT NULL)
ORDER BY ITEM_ID DESC;

select info.item_id, item_name, rarity
    from item_info info
    left join item_tree tree 
    on info.item_id = tree.parent_item_id
where parent_item_id is null
order by item_id desc;

