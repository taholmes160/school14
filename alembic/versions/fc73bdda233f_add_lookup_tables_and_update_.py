"""Add lookup tables and update StudentProfile model

Revision ID: fc73bdda233f
Revises: 3fcdfcc39a92
Create Date: 2024-09-09 17:30:53.664263

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = 'fc73bdda233f'
down_revision: Union[str, None] = '3fcdfcc39a92'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('active_duty_parents',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('bus_route_districts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('bus_route_numbers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('citizenship_statuses',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('club_memberships',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('current_grade_levels',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=10), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('custodial_arrangements',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('device_ownerships',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('disability_type_primaries',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('disability_type_secondaries',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('disability_type_tertiaries',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('enrollment_statuses',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('exit_withdrawal_statuses',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('exit_withdrawal_types',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('family_income_brackets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('family_structures',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('foster_care_involvements',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('gender_identities',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('homeless_statuses',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('iep_statuses',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('immigration_statuses',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('internet_accesses',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('migrant_education_programs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('non_promotion_reasons',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('other_languages',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('parent_education_levels',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('parent_life_statuses',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('parent_occupations',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('primary_languages',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('pronouns',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('religious_affiliations',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('sports_team_participations',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('states',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('tribal_affiliations',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('veteran_status_parents',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.add_column('student_profiles', sa.Column('grade_id', sa.Integer(), nullable=True))
    op.add_column('student_profiles', sa.Column('pronoun_id', sa.Integer(), nullable=True))
    op.add_column('student_profiles', sa.Column('family_structure_id', sa.Integer(), nullable=True))
    op.add_column('student_profiles', sa.Column('custodial_arrangement_id', sa.Integer(), nullable=True))
    op.add_column('student_profiles', sa.Column('primary_language_id', sa.Integer(), nullable=True))
    op.add_column('student_profiles', sa.Column('other_language_id', sa.Integer(), nullable=True))
    op.add_column('student_profiles', sa.Column('citizenship_status_id', sa.Integer(), nullable=True))
    op.add_column('student_profiles', sa.Column('immigration_status_id', sa.Integer(), nullable=True))
    op.add_column('student_profiles', sa.Column('family_income_bracket_id', sa.Integer(), nullable=True))
    op.add_column('student_profiles', sa.Column('parent_education_level_id', sa.Integer(), nullable=True))
    op.add_column('student_profiles', sa.Column('parent_occupation_id', sa.Integer(), nullable=True))
    op.add_column('student_profiles', sa.Column('current_grade_level_id', sa.Integer(), nullable=True))
    op.add_column('student_profiles', sa.Column('iep_status_id', sa.Integer(), nullable=True))
    op.add_column('student_profiles', sa.Column('bus_route_district_id', sa.Integer(), nullable=True))
    op.add_column('student_profiles', sa.Column('bus_route_number_id', sa.Integer(), nullable=True))
    op.add_column('student_profiles', sa.Column('sports_team_participation_id', sa.Integer(), nullable=True))
    op.add_column('student_profiles', sa.Column('club_membership_id', sa.Integer(), nullable=True))
    op.add_column('student_profiles', sa.Column('internet_access_id', sa.Integer(), nullable=True))
    op.add_column('student_profiles', sa.Column('device_ownership_id', sa.Integer(), nullable=True))
    op.add_column('student_profiles', sa.Column('active_duty_parent_id', sa.Integer(), nullable=True))
    op.add_column('student_profiles', sa.Column('veteran_status_parent_id', sa.Integer(), nullable=True))
    op.add_column('student_profiles', sa.Column('homeless_status_id', sa.Integer(), nullable=True))
    op.add_column('student_profiles', sa.Column('migrant_education_program_id', sa.Integer(), nullable=True))
    op.add_column('student_profiles', sa.Column('foster_care_involvement_id', sa.Integer(), nullable=True))
    op.add_column('student_profiles', sa.Column('tribe_membership_id', sa.Integer(), nullable=True))
    op.add_column('student_profiles', sa.Column('religious_affiliation_id', sa.Integer(), nullable=True))
    op.add_column('student_profiles', sa.Column('gender_identity_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'student_profiles', 'other_languages', ['other_language_id'], ['id'])
    op.create_foreign_key(None, 'student_profiles', 'family_structures', ['family_structure_id'], ['id'])
    op.create_foreign_key(None, 'student_profiles', 'gender_identities', ['gender_identity_id'], ['id'])
    op.create_foreign_key(None, 'student_profiles', 'club_memberships', ['club_membership_id'], ['id'])
    op.create_foreign_key(None, 'student_profiles', 'device_ownerships', ['device_ownership_id'], ['id'])
    op.create_foreign_key(None, 'student_profiles', 'family_income_brackets', ['family_income_bracket_id'], ['id'])
    op.create_foreign_key(None, 'student_profiles', 'religious_affiliations', ['religious_affiliation_id'], ['id'])
    op.create_foreign_key(None, 'student_profiles', 'custodial_arrangements', ['custodial_arrangement_id'], ['id'])
    op.create_foreign_key(None, 'student_profiles', 'citizenship_statuses', ['citizenship_status_id'], ['id'])
    op.create_foreign_key(None, 'student_profiles', 'iep_statuses', ['iep_status_id'], ['id'])
    op.create_foreign_key(None, 'student_profiles', 'parent_occupations', ['parent_occupation_id'], ['id'])
    op.create_foreign_key(None, 'student_profiles', 'tribal_affiliations', ['tribe_membership_id'], ['id'])
    op.create_foreign_key(None, 'student_profiles', 'current_grade_levels', ['grade_id'], ['id'])
    op.create_foreign_key(None, 'student_profiles', 'bus_route_districts', ['bus_route_district_id'], ['id'])
    op.create_foreign_key(None, 'student_profiles', 'veteran_status_parents', ['veteran_status_parent_id'], ['id'])
    op.create_foreign_key(None, 'student_profiles', 'migrant_education_programs', ['migrant_education_program_id'], ['id'])
    op.create_foreign_key(None, 'student_profiles', 'parent_education_levels', ['parent_education_level_id'], ['id'])
    op.create_foreign_key(None, 'student_profiles', 'homeless_statuses', ['homeless_status_id'], ['id'])
    op.create_foreign_key(None, 'student_profiles', 'bus_route_numbers', ['bus_route_number_id'], ['id'])
    op.create_foreign_key(None, 'student_profiles', 'sports_team_participations', ['sports_team_participation_id'], ['id'])
    op.create_foreign_key(None, 'student_profiles', 'internet_accesses', ['internet_access_id'], ['id'])
    op.create_foreign_key(None, 'student_profiles', 'immigration_statuses', ['immigration_status_id'], ['id'])
    op.create_foreign_key(None, 'student_profiles', 'active_duty_parents', ['active_duty_parent_id'], ['id'])
    op.create_foreign_key(None, 'student_profiles', 'foster_care_involvements', ['foster_care_involvement_id'], ['id'])
    op.create_foreign_key(None, 'student_profiles', 'primary_languages', ['primary_language_id'], ['id'])
    op.create_foreign_key(None, 'student_profiles', 'pronouns', ['pronoun_id'], ['id'])
    op.create_foreign_key(None, 'student_profiles', 'current_grade_levels', ['current_grade_level_id'], ['id'])
    op.drop_column('student_profiles', 'church_affiliation')
    op.drop_column('student_profiles', 'gender')
    op.drop_column('student_profiles', 'family_income_bracket')
    op.drop_column('student_profiles', 'iep_status')
    op.drop_column('student_profiles', 'grade')
    op.drop_column('student_profiles', 'veteran_status_parent')
    op.drop_column('student_profiles', 'custodial_arrangements')
    op.drop_column('student_profiles', 'migrant_education_program')
    op.drop_column('student_profiles', 'bus_route_number')
    op.drop_column('student_profiles', 'device_ownership')
    op.drop_column('student_profiles', 'internet_access')
    op.drop_column('student_profiles', 'active_duty_military_parent')
    op.drop_column('student_profiles', 'foster_care_involvement')
    op.drop_column('student_profiles', 'sports_team_participation')
    op.drop_column('student_profiles', 'other_languages')
    op.drop_column('student_profiles', 'parent_occupation')
    op.drop_column('student_profiles', 'family_structure')
    op.drop_column('student_profiles', 'homeless_status')
    op.drop_column('student_profiles', 'citizenship_status')
    op.drop_column('student_profiles', 'religious_affiliation')
    op.drop_column('student_profiles', 'current_grade_level')
    op.drop_column('student_profiles', 'parent_education_level')
    op.drop_column('student_profiles', 'tribe_membership')
    op.drop_column('student_profiles', 'club_memberships')
    op.drop_column('student_profiles', 'gender_identity')
    op.drop_column('student_profiles', 'immigration_status')
    op.drop_column('student_profiles', 'primary_language')
    op.drop_column('student_profiles', 'pronouns')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('student_profiles', sa.Column('pronouns', mysql.VARCHAR(length=50), nullable=True))
    op.add_column('student_profiles', sa.Column('primary_language', mysql.VARCHAR(length=50), nullable=True))
    op.add_column('student_profiles', sa.Column('immigration_status', mysql.VARCHAR(length=50), nullable=True))
    op.add_column('student_profiles', sa.Column('gender_identity', mysql.VARCHAR(length=50), nullable=True))
    op.add_column('student_profiles', sa.Column('club_memberships', mysql.TEXT(), nullable=True))
    op.add_column('student_profiles', sa.Column('tribe_membership', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True))
    op.add_column('student_profiles', sa.Column('parent_education_level', mysql.VARCHAR(length=50), nullable=True))
    op.add_column('student_profiles', sa.Column('current_grade_level', mysql.VARCHAR(length=10), nullable=True))
    op.add_column('student_profiles', sa.Column('religious_affiliation', mysql.VARCHAR(length=50), nullable=True))
    op.add_column('student_profiles', sa.Column('citizenship_status', mysql.VARCHAR(length=50), nullable=True))
    op.add_column('student_profiles', sa.Column('homeless_status', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True))
    op.add_column('student_profiles', sa.Column('family_structure', mysql.VARCHAR(length=50), nullable=True))
    op.add_column('student_profiles', sa.Column('parent_occupation', mysql.VARCHAR(length=50), nullable=True))
    op.add_column('student_profiles', sa.Column('other_languages', mysql.VARCHAR(length=50), nullable=True))
    op.add_column('student_profiles', sa.Column('sports_team_participation', mysql.TEXT(), nullable=True))
    op.add_column('student_profiles', sa.Column('foster_care_involvement', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True))
    op.add_column('student_profiles', sa.Column('active_duty_military_parent', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True))
    op.add_column('student_profiles', sa.Column('internet_access', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True))
    op.add_column('student_profiles', sa.Column('device_ownership', mysql.VARCHAR(length=50), nullable=True))
    op.add_column('student_profiles', sa.Column('bus_route_number', mysql.VARCHAR(length=50), nullable=True))
    op.add_column('student_profiles', sa.Column('migrant_education_program', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True))
    op.add_column('student_profiles', sa.Column('custodial_arrangements', mysql.TEXT(), nullable=True))
    op.add_column('student_profiles', sa.Column('veteran_status_parent', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True))
    op.add_column('student_profiles', sa.Column('grade', mysql.VARCHAR(length=10), nullable=True))
    op.add_column('student_profiles', sa.Column('iep_status', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True))
    op.add_column('student_profiles', sa.Column('family_income_bracket', mysql.VARCHAR(length=50), nullable=True))
    op.add_column('student_profiles', sa.Column('gender', mysql.VARCHAR(length=50), nullable=True))
    op.add_column('student_profiles', sa.Column('church_affiliation', mysql.VARCHAR(length=50), nullable=True))
    op.drop_constraint(None, 'student_profiles', type_='foreignkey')
    op.drop_constraint(None, 'student_profiles', type_='foreignkey')
    op.drop_constraint(None, 'student_profiles', type_='foreignkey')
    op.drop_constraint(None, 'student_profiles', type_='foreignkey')
    op.drop_constraint(None, 'student_profiles', type_='foreignkey')
    op.drop_constraint(None, 'student_profiles', type_='foreignkey')
    op.drop_constraint(None, 'student_profiles', type_='foreignkey')
    op.drop_constraint(None, 'student_profiles', type_='foreignkey')
    op.drop_constraint(None, 'student_profiles', type_='foreignkey')
    op.drop_constraint(None, 'student_profiles', type_='foreignkey')
    op.drop_constraint(None, 'student_profiles', type_='foreignkey')
    op.drop_constraint(None, 'student_profiles', type_='foreignkey')
    op.drop_constraint(None, 'student_profiles', type_='foreignkey')
    op.drop_constraint(None, 'student_profiles', type_='foreignkey')
    op.drop_constraint(None, 'student_profiles', type_='foreignkey')
    op.drop_constraint(None, 'student_profiles', type_='foreignkey')
    op.drop_constraint(None, 'student_profiles', type_='foreignkey')
    op.drop_constraint(None, 'student_profiles', type_='foreignkey')
    op.drop_constraint(None, 'student_profiles', type_='foreignkey')
    op.drop_constraint(None, 'student_profiles', type_='foreignkey')
    op.drop_constraint(None, 'student_profiles', type_='foreignkey')
    op.drop_constraint(None, 'student_profiles', type_='foreignkey')
    op.drop_constraint(None, 'student_profiles', type_='foreignkey')
    op.drop_constraint(None, 'student_profiles', type_='foreignkey')
    op.drop_constraint(None, 'student_profiles', type_='foreignkey')
    op.drop_constraint(None, 'student_profiles', type_='foreignkey')
    op.drop_constraint(None, 'student_profiles', type_='foreignkey')
    op.drop_column('student_profiles', 'gender_identity_id')
    op.drop_column('student_profiles', 'religious_affiliation_id')
    op.drop_column('student_profiles', 'tribe_membership_id')
    op.drop_column('student_profiles', 'foster_care_involvement_id')
    op.drop_column('student_profiles', 'migrant_education_program_id')
    op.drop_column('student_profiles', 'homeless_status_id')
    op.drop_column('student_profiles', 'veteran_status_parent_id')
    op.drop_column('student_profiles', 'active_duty_parent_id')
    op.drop_column('student_profiles', 'device_ownership_id')
    op.drop_column('student_profiles', 'internet_access_id')
    op.drop_column('student_profiles', 'club_membership_id')
    op.drop_column('student_profiles', 'sports_team_participation_id')
    op.drop_column('student_profiles', 'bus_route_number_id')
    op.drop_column('student_profiles', 'bus_route_district_id')
    op.drop_column('student_profiles', 'iep_status_id')
    op.drop_column('student_profiles', 'current_grade_level_id')
    op.drop_column('student_profiles', 'parent_occupation_id')
    op.drop_column('student_profiles', 'parent_education_level_id')
    op.drop_column('student_profiles', 'family_income_bracket_id')
    op.drop_column('student_profiles', 'immigration_status_id')
    op.drop_column('student_profiles', 'citizenship_status_id')
    op.drop_column('student_profiles', 'other_language_id')
    op.drop_column('student_profiles', 'primary_language_id')
    op.drop_column('student_profiles', 'custodial_arrangement_id')
    op.drop_column('student_profiles', 'family_structure_id')
    op.drop_column('student_profiles', 'pronoun_id')
    op.drop_column('student_profiles', 'grade_id')
    op.drop_table('veteran_status_parents')
    op.drop_table('tribal_affiliations')
    op.drop_table('states')
    op.drop_table('sports_team_participations')
    op.drop_table('religious_affiliations')
    op.drop_table('pronouns')
    op.drop_table('primary_languages')
    op.drop_table('parent_occupations')
    op.drop_table('parent_life_statuses')
    op.drop_table('parent_education_levels')
    op.drop_table('other_languages')
    op.drop_table('non_promotion_reasons')
    op.drop_table('migrant_education_programs')
    op.drop_table('internet_accesses')
    op.drop_table('immigration_statuses')
    op.drop_table('iep_statuses')
    op.drop_table('homeless_statuses')
    op.drop_table('gender_identities')
    op.drop_table('foster_care_involvements')
    op.drop_table('family_structures')
    op.drop_table('family_income_brackets')
    op.drop_table('exit_withdrawal_types')
    op.drop_table('exit_withdrawal_statuses')
    op.drop_table('enrollment_statuses')
    op.drop_table('disability_type_tertiaries')
    op.drop_table('disability_type_secondaries')
    op.drop_table('disability_type_primaries')
    op.drop_table('device_ownerships')
    op.drop_table('custodial_arrangements')
    op.drop_table('current_grade_levels')
    op.drop_table('club_memberships')
    op.drop_table('citizenship_statuses')
    op.drop_table('bus_route_numbers')
    op.drop_table('bus_route_districts')
    op.drop_table('active_duty_parents')
    # ### end Alembic commands ###
