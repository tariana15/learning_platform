PGDMP  1            	        |            academy    17.2    17.0 )    !           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                           false            "           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                           false            #           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                           false            $           1262    16390    academy    DATABASE     {   CREATE DATABASE academy WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'Russian_Russia.1251';
    DROP DATABASE academy;
                     postgres    false            �            1259    16391    alembic_version    TABLE     X   CREATE TABLE public.alembic_version (
    version_num character varying(32) NOT NULL
);
 #   DROP TABLE public.alembic_version;
       public         heap r       postgres    false            �            1259    16466    results    TABLE     �   CREATE TABLE public.results (
    student_id integer NOT NULL,
    student_result character varying NOT NULL,
    test_number integer NOT NULL,
    id integer NOT NULL
);
    DROP TABLE public.results;
       public         heap r       postgres    false            �            1259    16531    results_id_seq    SEQUENCE     |   CREATE SEQUENCE public.results_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    MAXVALUE 5000000
    CACHE 1;
 %   DROP SEQUENCE public.results_id_seq;
       public               postgres    false    218            %           0    0    results_id_seq    SEQUENCE OWNED BY     A   ALTER SEQUENCE public.results_id_seq OWNED BY public.results.id;
          public               postgres    false    225            �            1259    16471    roles    TABLE        CREATE TABLE public.roles (
    id integer NOT NULL,
    name character varying(80),
    description character varying(255)
);
    DROP TABLE public.roles;
       public         heap r       postgres    false            �            1259    16474    roles_id_seq    SEQUENCE     �   CREATE SEQUENCE public.roles_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 #   DROP SEQUENCE public.roles_id_seq;
       public               postgres    false    219            &           0    0    roles_id_seq    SEQUENCE OWNED BY     =   ALTER SEQUENCE public.roles_id_seq OWNED BY public.roles.id;
          public               postgres    false    220            �            1259    16475    roles_users    TABLE     N   CREATE TABLE public.roles_users (
    user_id integer,
    role_id integer
);
    DROP TABLE public.roles_users;
       public         heap r       postgres    false            �            1259    16478    teachers_students    TABLE     l   CREATE TABLE public.teachers_students (
    teacher_id integer NOT NULL,
    student_id integer NOT NULL
);
 %   DROP TABLE public.teachers_students;
       public         heap r       postgres    false            �            1259    16481    users    TABLE       CREATE TABLE public.users (
    id integer NOT NULL,
    name character varying,
    username character varying,
    email character varying,
    password character varying,
    created_on timestamp without time zone,
    updated_on timestamp without time zone,
    active boolean
);
    DROP TABLE public.users;
       public         heap r       postgres    false            �            1259    16486    users_id_seq    SEQUENCE     �   CREATE SEQUENCE public.users_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 #   DROP SEQUENCE public.users_id_seq;
       public               postgres    false    223            '           0    0    users_id_seq    SEQUENCE OWNED BY     =   ALTER SEQUENCE public.users_id_seq OWNED BY public.users.id;
          public               postgres    false    224            m           2604    16532 
   results id    DEFAULT     h   ALTER TABLE ONLY public.results ALTER COLUMN id SET DEFAULT nextval('public.results_id_seq'::regclass);
 9   ALTER TABLE public.results ALTER COLUMN id DROP DEFAULT;
       public               postgres    false    225    218            n           2604    16487    roles id    DEFAULT     d   ALTER TABLE ONLY public.roles ALTER COLUMN id SET DEFAULT nextval('public.roles_id_seq'::regclass);
 7   ALTER TABLE public.roles ALTER COLUMN id DROP DEFAULT;
       public               postgres    false    220    219            o           2604    16488    users id    DEFAULT     d   ALTER TABLE ONLY public.users ALTER COLUMN id SET DEFAULT nextval('public.users_id_seq'::regclass);
 7   ALTER TABLE public.users ALTER COLUMN id DROP DEFAULT;
       public               postgres    false    224    223                      0    16391    alembic_version 
   TABLE DATA           6   COPY public.alembic_version (version_num) FROM stdin;
    public               postgres    false    217   �-                 0    16466    results 
   TABLE DATA           N   COPY public.results (student_id, student_result, test_number, id) FROM stdin;
    public               postgres    false    218   �-                 0    16471    roles 
   TABLE DATA           6   COPY public.roles (id, name, description) FROM stdin;
    public               postgres    false    219   ".                 0    16475    roles_users 
   TABLE DATA           7   COPY public.roles_users (user_id, role_id) FROM stdin;
    public               postgres    false    221   f.                 0    16478    teachers_students 
   TABLE DATA           C   COPY public.teachers_students (teacher_id, student_id) FROM stdin;
    public               postgres    false    222   �.                 0    16481    users 
   TABLE DATA           d   COPY public.users (id, name, username, email, password, created_on, updated_on, active) FROM stdin;
    public               postgres    false    223   �.       (           0    0    results_id_seq    SEQUENCE SET     =   SELECT pg_catalog.setval('public.results_id_seq', 10, true);
          public               postgres    false    225            )           0    0    roles_id_seq    SEQUENCE SET     ;   SELECT pg_catalog.setval('public.roles_id_seq', 1, false);
          public               postgres    false    220            *           0    0    users_id_seq    SEQUENCE SET     :   SELECT pg_catalog.setval('public.users_id_seq', 3, true);
          public               postgres    false    224            q           2606    16395 #   alembic_version alembic_version_pkc 
   CONSTRAINT     j   ALTER TABLE ONLY public.alembic_version
    ADD CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num);
 M   ALTER TABLE ONLY public.alembic_version DROP CONSTRAINT alembic_version_pkc;
       public                 postgres    false    217            s           2606    16490    results results_pkey 
   CONSTRAINT     R   ALTER TABLE ONLY public.results
    ADD CONSTRAINT results_pkey PRIMARY KEY (id);
 >   ALTER TABLE ONLY public.results DROP CONSTRAINT results_pkey;
       public                 postgres    false    218            u           2606    16492    roles roles_name_key 
   CONSTRAINT     O   ALTER TABLE ONLY public.roles
    ADD CONSTRAINT roles_name_key UNIQUE (name);
 >   ALTER TABLE ONLY public.roles DROP CONSTRAINT roles_name_key;
       public                 postgres    false    219            w           2606    16494    roles roles_pkey 
   CONSTRAINT     N   ALTER TABLE ONLY public.roles
    ADD CONSTRAINT roles_pkey PRIMARY KEY (id);
 :   ALTER TABLE ONLY public.roles DROP CONSTRAINT roles_pkey;
       public                 postgres    false    219            y           2606    16496 (   teachers_students teachers_students_pkey 
   CONSTRAINT     z   ALTER TABLE ONLY public.teachers_students
    ADD CONSTRAINT teachers_students_pkey PRIMARY KEY (teacher_id, student_id);
 R   ALTER TABLE ONLY public.teachers_students DROP CONSTRAINT teachers_students_pkey;
       public                 postgres    false    222    222            {           2606    16498    users users_email_key 
   CONSTRAINT     Q   ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_email_key UNIQUE (email);
 ?   ALTER TABLE ONLY public.users DROP CONSTRAINT users_email_key;
       public                 postgres    false    223            }           2606    16500    users users_pkey 
   CONSTRAINT     N   ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);
 :   ALTER TABLE ONLY public.users DROP CONSTRAINT users_pkey;
       public                 postgres    false    223                       2606    16502    users users_username_key 
   CONSTRAINT     W   ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_username_key UNIQUE (username);
 B   ALTER TABLE ONLY public.users DROP CONSTRAINT users_username_key;
       public                 postgres    false    223            �           2606    16503    teachers_students fk_student    FK CONSTRAINT     ~   ALTER TABLE ONLY public.teachers_students
    ADD CONSTRAINT fk_student FOREIGN KEY (student_id) REFERENCES public.users(id);
 F   ALTER TABLE ONLY public.teachers_students DROP CONSTRAINT fk_student;
       public               postgres    false    222    223    4733            �           2606    16508    results fk_student    FK CONSTRAINT     ~   ALTER TABLE ONLY public.results
    ADD CONSTRAINT fk_student FOREIGN KEY (student_id) REFERENCES public.users(id) NOT VALID;
 <   ALTER TABLE ONLY public.results DROP CONSTRAINT fk_student;
       public               postgres    false    223    218    4733            �           2606    16513    teachers_students fk_teacher    FK CONSTRAINT     ~   ALTER TABLE ONLY public.teachers_students
    ADD CONSTRAINT fk_teacher FOREIGN KEY (teacher_id) REFERENCES public.users(id);
 F   ALTER TABLE ONLY public.teachers_students DROP CONSTRAINT fk_teacher;
       public               postgres    false    222    223    4733            �           2606    16518 $   roles_users roles_users_role_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.roles_users
    ADD CONSTRAINT roles_users_role_id_fkey FOREIGN KEY (role_id) REFERENCES public.roles(id);
 N   ALTER TABLE ONLY public.roles_users DROP CONSTRAINT roles_users_role_id_fkey;
       public               postgres    false    4727    219    221            �           2606    16523 $   roles_users roles_users_user_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.roles_users
    ADD CONSTRAINT roles_users_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(id);
 N   ALTER TABLE ONLY public.roles_users DROP CONSTRAINT roles_users_user_id_fkey;
       public               postgres    false    221    4733    223               '   x�3706K1�H4�HK�H6��4OM51�L����� |�=         K   x�5���0г��!�g��?G1�pyB��;�kפ��vl+3�,�ʳ2gZqݯ�c���<f~�{��� �         4   x�3�LL����
)���\F��%�)�y%`"f�Y�����Z�!�1z\\\ �w�            x�3�4�2�4�2�=... F            x�3�4����� t!         �  x�}��jTA���Sd1�u��R#0%n�V&Q����\��#�w�y#	�0���_t�W��'��x����������]��,�b��c>�0?��,����r`2�Cpv�s����?}��:k�f��S�TC��ي��P��4���R

][��D�u-�R�XE��,J!{o�k� ��V)�+�V��X�ěNH��)n!`�<)�Ȧh9�;��v�y��\��_�����<����7�/�_|Z�^�� �&�M��`�'	Čĩ���&�k���dF��b��F��0N��@��2K�.��ܫ�'�&Պa3���]%y�Z�[h� 8�hS������<=�����������<y�o�s}�N����zR��;���JkM=��ݬJ%����B�8�-y���x8w�X<���Bd��j���#5�Ҋ��Do���g��J�-�o����7��     