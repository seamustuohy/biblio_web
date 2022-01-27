from django.shortcuts import render

# Create your views here.
from . import forms
from . import utils
from os import environ
from pathlib import Path
from biblio.query import get_file_info_from_database
from biblio.utils import get_database, get_file_id
from biblio.update import update_object_info
from django.http import Http404


import logging
logging.basicConfig(level=logging.ERROR)
log = logging.getLogger(__name__)

def UpdateForm(request):
    #Check to see if we are getting a POST request back
    if request.method == "POST":
        form = forms.UpdateDocInfoForm(request.POST)
        if form.is_valid():
            # Then we check to see if the form is valid (this is an automatic validation by Django)
            # if form.is_valid == True then do something
            # print("Form validation successful!")
            file_path = request.GET.get('file_path', '')
            properties = form.cleaned_data
            # print(properties)
            # print("FILE PATH")
            # print(file_path)
            object_uid = get_file_id(file_path)
            # print(object_uid)
            dbpath = environ['BiblioDBPath']
            db = get_database(dbpath)
            try:
                update_object_info(db, object_uid, properties)
            except:
                form.add_error(None, "An error occurred when attempting to update the object in the database.")
    elif request.method == "GET":
        try:
            path_q = request.GET.get('file_path', '')
            # print(path_q)
            # print(path_q is None)
            if path_q != "":
                file_path = Path(path_q).resolve()
                # print(file_path)
                file_path = file_path.resolve(strict=True)
                if file_path.parent.relative_to(environ['BiblioArchiveDir']):
                    dbpath = environ['BiblioDBPath']
                    db = get_database(dbpath)
                    file_path = str(file_path)
                    # print(file_path)
                    initial_data = get_file_info_from_database(file_path, db)
                    db.close()
                    # print("INITIAL DATA")
                    # print(initial_data)
                    form = forms.UpdateDocInfoForm(initial=initial_data['object'])
                else:
                    raise FileNotFoundError("Invalid file path supplied")
            else:
                raise FileNotFoundError("The form cannot be called without a valid file path. Your link to this form was bad and you should feel bad")
        except FileNotFoundError as _e:
            raise Http404

    try:
        archive_dir = environ["BiblioArchiveDir"]
    except KeyError as e:
        raise RuntimeError("Could not find a BiblioArchiveDir in environment. This is needed to know where to serve static archive files from.") from e
    try:
        archive_prefix = environ["BiblioStaticArchivePrefix"]
    except KeyError as e:
        raise RuntimeError("Could not find a BiblioArchiveDir in environment. This is needed to know where to serve static archive files from.") from e

    archive_path = file_path.replace(archive_dir, archive_prefix)
    return render(request, 'forms/update_form.html', {'form': form,
                                                      'pdf': archive_path})
