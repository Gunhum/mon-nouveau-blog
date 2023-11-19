from django.shortcuts import render,get_object_or_404, redirect
from .models import Equipement, Character
from .forms import MoveForm

def post_list(request):
    joueurs = Character.objects.all()
    equip = Equipement.objects.all()
    return render(request, 'tennisclub/post_list.html', {'joueurs': joueurs,'equipements':equip})


def character_detail(request, id_character,message = ""):
    character = get_object_or_404(Character, id_character=id_character)
    lieu = character.lieu
    if request.method == "POST":
        form = MoveForm(request.POST, instance=character)
        if form.is_valid():
            nouveau_lieu = get_object_or_404(Equipement, id_equip=character.lieu.id_equip)
            if nouveau_lieu.disponibilite == "libre":
                lieu.place += 1
                lieu.disponibilite = "libre"    
                lieu.save()
                nouveau_lieu.place = nouveau_lieu.place - 1
                if nouveau_lieu.place == 0:
                    nouveau_lieu.disponibilite = "occupe"
                nouveau_lieu.save()
                character.lieu = nouveau_lieu
                if nouveau_lieu.id_equip == "Bar":
                    character.etat = "revigore"
                if nouveau_lieu.id_equip == "Terrain1" or nouveau_lieu == "Terrain2":
                    character.etat = "fatigue"
                if nouveau_lieu.id_equip == "Vestiaire":
                    character.etat = "pret"
                character.save()
                form.save()
                message = f"{character.prenom} quitte le {lieu.id_equip} pour aller au {nouveau_lieu.id_equip}"
            else:
                form.save(commit=False) 
                message = f"Il n'y plus de place au {nouveau_lieu.id_equip}. {character.prenom} reste au {lieu.id_equip}"
            return redirect('character_detail_mes', id_character=id_character, message = message)
    else:
        form = MoveForm()
        return render(request,'tennisclub/character_detail.html',{'character': character, 'lieu': lieu, 'form': form,'message': message})