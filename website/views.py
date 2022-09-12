
from . import db
from flask import Blueprint, render_template,flash,request,jsonify, redirect, url_for
from flask_login import login_user,login_required,current_user
from .models import Project, members_in_project, User
import json

views = Blueprint('views',__name__)

# Register the Blueprints in __init__.py



@views.route('/',methods=['GET','POST'])
@login_required
def home():
    if request.method == 'POST':
        project_title = request.form.get('project_title')
        project_details = request.form.get('project_details')
        
        
        if project_title != None and len(project_title) < 1:
            flash('Project title needs to be longer',category='error')
        title_name = Project.query.filter_by(name=project_title).first()
        if title_name:
            flash('Project title already exists. Try different title', category='error')
            
        else:
            new_project = Project(name = project_title, description = project_details, owner_id = current_user.id)
            db.session.add(new_project)
            db.session.commit()
            flash('Project added', category='success')
    all_projects = Project.query.all()
 
        
    return render_template('home.html',user=current_user, all_projects = all_projects)


@views.route('/delete_project', methods=['GET','POST'])
@login_required
def delete_project():
    print("$$$$$$")
    get_proj_id = request.form.get('project_id')
    if get_proj_id is not None:
        project_to_delete = Project.query.get(get_proj_id)
        # all_projects = Project.query.all()
        db.session.delete(project_to_delete)
        db.session.commit()
        flash('Deleted the project!', category='success')
        return redirect(url_for('views.home')) #url stays delete_project?
        # return render_template('home.html', user=current_user,all_projects = all_projects)

@views.route('/join_project', methods=['GET','POST'])
@login_required
def join_project():
    if request.method == 'POST':
        get_proj_id = request.form.get('project_id')
        if get_proj_id is not None:
            user = current_user
            project = Project.query.get(get_proj_id)
            project.members.append(user)
            db.session.add(project)
            db.session.commit()
            flash('Joined the project!', category='success')
            return redirect(url_for('views.home'))