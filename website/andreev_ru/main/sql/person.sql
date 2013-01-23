CREATE FULLTEXT INDEX person_name_ru ON main_person (name_ru);
CREATE FULLTEXT INDEX person_name_en ON main_person (name_en);

CREATE FULLTEXT INDEX person_bio_ru ON main_person (bio_ru);
CREATE FULLTEXT INDEX person_bio_en ON main_person (bio_en);
