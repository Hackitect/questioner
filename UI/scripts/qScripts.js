function ConfirmDelete()
{
    var x = confirm("Are you sure you want to delete this meetup?");
    if (x)
        return true;
    else
        return false;
}

function deleteMeetup() {
    var elem = document.getElementById('meetup');
    elem.parentNode.removeChild(elem);
}