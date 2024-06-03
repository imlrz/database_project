USE TESTPROJ;
DELIMITER $
CREATE TRIGGER UPDATE_GRADE
AFTER INSERT ON catalog_comment
FOR EACH ROW
BEGIN
    DECLARE RESTA_AVG_GRADE FLOAT;
    DECLARE DISH_AVG_GRADE FLOAT;
    SELECT AVG(grade) INTO RESTA_AVG_GRADE FROM catalog_comment WHERE catalog_comment.resta_ID_id = NEW.resta_ID_id;
    UPDATE catalog_restaurant SET AVG_grade = RESTA_AVG_GRADE WHERE resta_ID = NEW.resta_ID_id;
    IF NEW.dish_ID_id != NULL THEN
		SELECT AVG(grade) INTO DISH_AVG_GRADE FROM catalog_comment WHERE catalog_comment.dish_ID_id = NEW.dish_ID_id;
        UPDATE catalog_dish SET AVG_grade = DISH_AVG_GRADE WHERE dish_ID = NEW.dish_ID_id;
	END IF;
    
END$
DELIMITER ;