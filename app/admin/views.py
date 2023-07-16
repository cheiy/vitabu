# app/admin/views.py

from flask import abort, flash, redirect, render_template, url_for, request
from flask_login import current_user, login_required

from . import admin
from .forms import PublisherForm, AddBookForm, AddGradeForm, AddSubjectForm
from .. import db
from ..models import Publisher, Book, Grade, Subject

def check_admin():
    """
    Prevent non-admins from accessing the page
    """
    if not current_user.is_admin:
        abort(403)

# Publishers Views

@admin.route('/publishers', methods=['GET', 'POST'])
@login_required
def list_publishers():
    """
    List all publishers
    """
    check_admin()

    publishers = Publisher.query.all()

    return render_template('admin/publishers/publishers.html',
                           publishers=publishers, title="publishers")

@admin.route('/publishers/add', methods=['GET', 'POST'])
@login_required
def add_publisher():
    """
    Add a publisher to the database
    """
    check_admin()

    add_publisher = True

    form = PublisherForm()
    if form.validate_on_submit():
        publisher = Publisher(shortname=form.shortname.data,
                                longname=form.longname.data,
                                        ISBN=form.isbn.data)
        try:
            # add publisher to the database
            db.session.add(publisher)
            db.session.commit()
            flash('You have successfully added a new publisher.')
        except:
            # in case publisher name already exists
            flash('Error: publisher name already exists.')

        # redirect to publishers page
        return redirect(url_for('admin.list_publishers'))

    # load publisher template
    return render_template('admin/publishers/publisher.html', action="Add",
                           add_publisher=add_publisher, form=form,
                           title="Add Publisher")

@admin.route('/publishers/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_publisher(id):
    """
    Edit a publisher
    """
    check_admin()

    add_publisher = False

    publisher = Publisher.query.get_or_404(id)
    form = PublisherForm(obj=publisher)
    if form.validate_on_submit():
        publisher.shortname = form.shortname.data
        publisher.longname = form.longname.data
        publisher.ISBN = form.ISBN.data
        
        #db.session.add(publisher)
        db.session.commit()
        flash('You have successfully edited the publisher.')

        # redirect to the publishers page
        return redirect(url_for('admin.list_publishers'))
    
    #form.longname.data = publisher.longname
    #form.shortname.data = publisher.shortname
    #form.isbn.data = publisher.ISBN
    return render_template('admin/publishers/publisher.html', action="Edit",
                           add_publisher=add_publisher, form=form,
                           publisher=publisher, title="Edit Publisher")

@admin.route('/publishers/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_publisher(id):
    """
    Delete a publisher from the database
    """
    check_admin()

    publisher = Publisher.query.get_or_404(id)
    db.session.delete(publisher)
    db.session.commit()
    flash('You have successfully deleted the publisher.')

    # redirect to the publishers page
    return redirect(url_for('admin.list_publishers'))

    return render_template(title="Delete Publisher")

@admin.route('/books', methods=['GET', 'POST'])
@login_required
def list_books():
    """
    List all books
    """
    check_admin()

    books = Book.query.all()
    #flash(books)
    return render_template('admin/books/books.html',
                           books=books, title="books")


#Add Book
@admin.route('/books/add', methods=['GET', 'POST'])
@login_required
def add_book():
    """
    Add a Book to the database
    """
    check_admin()

    add_book = True

    #grade = Grade.query.all()

    form = AddBookForm()
    """Autopopulate the Publisher's Field with names of the publishers"""
    publisher = Publisher.query.all()
    #form = AddBookForm(obj=publisher)
    form.publisher_id.choices = [(p.publisher_id, p.longname) for p in Publisher.query.order_by('publisher_id')]

    """Autopopulate the grade field with names of the grades"""
    grade = Grade.query.all()
    #form = AddBookForm(obj=grade)
    form.grade_id.choices = [(g.grade_id, g.grade_name) for g in Grade.query.order_by('grade_id')]

    """Autopopulate the subject field with names of the subjects"""
    subject = Subject.query.all()
    form.subject_id.choices = [(s.id, s.subject_name) for s in Subject.query.order_by('id')]
    
    """ENDSAM"""
    if form.validate_on_submit():

        book = Book(isbn_code=form.isbn_code.data,
                                title = form.title.data,
                                publisher_id = form.publisher_id.data,
                                grade_id = form.grade_id.data,
                                subject_id = form.subject_id.data)
        try:
            # add book to the database
            db.session.add(book)
            db.session.commit()
            flash('You have successfully added a new book.')
        except:
            # in case book name already exists
            flash('Error: book name already exists.')

        # redirect to books page
        return redirect(url_for('admin.list_books'))

    # load book template
    return render_template('admin/books/book.html', action="Add",
                           add_book=add_book, form=form,

                           title="Add Book")

# Edit Book
@admin.route('/books/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_book(id):
    """
    Edit book details
    """
    check_admin()
    
    add_book = False

    book = Book.query.get_or_404(id)
    form = AddBookForm(obj=book)

    """Autopopulate the Publisher's Field with names of the publishers"""
    #publisher = Publisher.query.all()
    #form = AddBookForm(obj=publisher)
    #form.publisher_id.choices = [(publisher_longname, publisher_id)]
    form.publisher_id.choices = [(p.publisher_id, p.longname) for p in Publisher.query.order_by('publisher_id')]
    """Autopopulate the grade field with names of the grades"""
    #grade = Grade.query.all()
    #form = AddBookForm(obj=grade)
    form.grade_id.choices = [(g.grade_id, g.grade_name) for g in Grade.query.order_by('grade_id')]

    """Autopopulate the subject field with names of the subjects"""
    #subject = Subject.query.all()
    form.subject_id.choices = [(s.id, s.subject_name) for s in Subject.query.order_by('id')]

    if form.validate_on_submit():
      
       book.isbn_code = form.isbn_code.data
       book.title = form.title.data
       book.publisher_id = form.publisher_id.data
       book.grade_id = form.grade_id.data
       book.subject_id = form.subject_id.data
       db.session.commit()
       flash('You have unsuccessfully edited the book.')

       # Redirect to the books page
       return redirect(url_for('admin.list_books'))
    form.isbn_code.data = book.isbn_code
    form.title.data = book.title
    form.publisher_id.data = book.publisher_id
    form.grade_id.data = book.grade_id
    form.subject_id.data = book.subject_id
    return render_template('admin/books/book.html', action="Edit",
                           add_book=add_book, form=form,
                           book=book, title="Edit Book")

# Delete Book
@admin.route('/books/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_book(id):
    """
    Delete Book
    """
    check_admin()

    add_book = False

    book = Book.query.get_or_404(id)
    db.session.delete(book)
    db.session.commit()
    flash('You have successfully deleted the book.')

    # redirect to the books page
    return redirect(url_for('admin.list_books'))
   
    return render_template(title="Delete Book")


# List Grades
@admin.route('/grades', methods=['GET', 'POST'])
@login_required
def list_grades():
    """
    List all Grades
    """
    check_admin()

    grades = Grade.query.all()

    return render_template('admin/grades/grades.html',
                           grades=grades, title="grades")


# Add Grades
@admin.route('/grades/add', methods=['GET', 'POST'])
@login_required
def add_grade():
    """
    Add Grades
    """
    check_admin()

    add_grade = True


    form = AddGradeForm()
    if form.validate_on_submit():
        grade = Grade(grade_num=form.grade_num.data,
                      grade_name = form.grade_name.data)

        try:
            # add book to the database
            db.session.add(grade)
            db.session.commit()
            flash('You have successfully added a new grade.')

        except:
            # in case book name already exists
            flash('Error: grade/class already exists.')

        # redirect to grades page
        return redirect(url_for('admin.list_grades'))

    # load grade template
    return render_template('admin/grades/grade.html', action="Add",
                           add_grade=add_grade, form=form,
                           title="Add Grade")

# Edit Grade
@admin.route('/grades/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_grade(id):
    """
    Edit a grade
    """
    check_admin()

    add_grade = False

    grade = Grade.query.get_or_404(id)
    form = AddGradeForm(obj=grade)
    if form.validate_on_submit():
        grade_num = form.grade_num.data
        grade_name = form.grade_name.data
        db.session.commit()
        flash('You have successfully edited the grade.')

        # redirect to the grades page
        return redirect(url_for('admin.list_publishers'))

    form.grade_num.data = grade.grade_num
    form.grade_name.data = grade.grade_name
    return render_template('admin/grades/grade.html', action="Edit",
                           add_grade=add_grade, form=form,
                           grade=grade, title="Edit Grade")


# Delete Grade
@admin.route('/grades/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_grade(id):
    """
    Delete a grade from the database
    """
    check_admin()

    grade = Grade.query.get_or_404(id)
    db.session.delete(grade)
    db.session.commit()
    flash('You have successfully deleted the Grade.')

    # redirect to the publishers page
    return redirect(url_for('admin.list_grades'))

    return render_template(title="Delete Grade")


# List Subjects
@admin.route('/subjects', methods=['GET', 'POST'])
@login_required
def list_subjects():
    """
    List all Subjects
    """
    check_admin()

    subjects = Subject.query.all()

    return render_template('admin/subjects/subjects.html',
                           subjects=subjects, title="subjects")


# Add Subject
@admin.route('/subjects/add', methods=['GET','POST'])
@login_required
def add_subject():

    check_admin()

    add_grade = True

    form = AddSubjectForm()
    if form.validate_on_submit():
        subject = Subject(subject_name=form.subject_name.data)

        try:
            # add book to the database
            db.session.add(subject)
            db.session.commit()
            flash('You have successfully added a new subject.')

        except:
            # in case subject name already exists
            flash('Error: subject already exists.')

        # redirect to subjects page
        return redirect(url_for('admin.list_subjects'))

    # load subject template
    return render_template('admin/subjects/subject.html', action="Add",
                           add_subject=add_subject, form=form,
                           title="Add Subject")


# Delete Subject
@admin.route('/subjects/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_subject(id):
    """
    Delete a subject from the database
    """
    check_admin()

    subject = Subject.query.get_or_404(id)
    db.session.delete(subject)
    db.session.commit()
    flash('You have successfully deleted the Subject.')

    # redirect to the subjects page
    return redirect(url_for('admin.list_subjects'))

    return render_template(title="Delete Subject")


# Edit Subject
@admin.route('/subjects/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_subject(id):
    """
    Edit a subject
    """
    check_admin()

    add_subject = False

    subject = Subject.query.get_or_404(id)
    form = AddSubjectForm(obj=subject)
    if form.validate_on_submit():
        subject_name = form.subject_name.data
        db.session.commit()
        flash('You have successfully edited the subject.')

        # redirect to the subjects page
        return redirect(url_for('admin.list_subjects'))

    form.subject_name.data = subject.subject_name
    return render_template('admin/subjects/subject.html', action="Edit",
                           add_subject=add_subject, form=form,
                           subject=subject, title="Edit Subject")

