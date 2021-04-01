from django.shortcuts import render
from .models import LiveVideo, Galery, TamuUndangan, Pengantin, Pesan
# Create your views here.
def index(request, nama):
    status = ""
    tamu_undangan = TamuUndangan.objects.get(nama=nama)
    if request.method == 'POST':
        ucap = request.POST['ucap']
        sumbang = request.POST['sumbang']
        Pesan.objects.create(
			nama = tamu_undangan,
		    ucapan = ucap,
		    sumbangan= sumbang,
		    tampilkan = True,
		)
        status = "Terimakasih Atas Ucapannya" 
        

    video = LiveVideo.objects.get(pk=1)
    galeries = Galery.objects.all() 
    pengantin_putra = Pengantin.objects.get(id=1)
    pengantin_putri = Pengantin.objects.get(id=2)
    pesans = Pesan.objects.all().order_by('-id')
    context = {
        'title' : 'Beranda',
        'SubJudul' : '',
  		'content'	: "",
        'video' : video,
        'galeries' : galeries,
        'tamu_undangan' : tamu_undangan,
        'pengantin_putra' : pengantin_putra,
        'pengantin_putri' : pengantin_putri,
        'pesans' : pesans,
        'status' : status,
    }
    return render(request, 'base.html', context)



def list_grup(request):
    tamu_undangan = TamuUndangan.objects.all()
    grups = []
    for data in tamu_undangan:

        if data.keterangan not in grups:
            grups.append(data.keterangan)


    context = {
        'title' : 'Beranda',
        'SubJudul' : '',
        'content'   : "",
        'grups'     : grups
        }
    print(grups)
    return render(request, 'list_grup.html', context)

def list_of_grup(request, grup):


    tamu_undangan = TamuUndangan.objects.filter(keterangan=grup)
    context = {
        
        'tamu_undangan' : tamu_undangan,
        
    }
    return render(request, 'list_of_grup.html', context)
