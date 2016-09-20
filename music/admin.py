from django.contrib import admin
from .models import Album, Track, Artist, Genre,TrackType

class AlbumAdmin(admin.ModelAdmin):
    
    search_fields = ['name','track__name']
    list_display = ['name','track_names']

    def track_names(self,obj):
        names = [track.name for track in obj.tracks.all()]
        return ", ".join(names)

    track_names.short_description = 'Tracks'

class AlbumInline(admin.StackedInline):
    model = Album.tracks.through
    extra = 0

class TrackAdmin(admin.ModelAdmin):
    
    search_fields = ['name','artists__name','album__name']
    list_display = ['name','album_names','artist_names','ttype']

    def artist_names(self,obj):
        names = [artist.name for artist in obj.artists.all()]
        return ", ".join(names)

    artist_names.short_description = 'Artists'

    def album_names(self,obj):
        names = [album.name for album in obj.album_set.all()]
        return ", ".join(names)

    album_names.short_description = 'Album'

    def ttype(self,obj):
        names = [t.category for t in obj.track_type.all()]
        return ", ".join(names)

    ttype.short_description = 'TrackType'

class TrackInline(admin.StackedInline):
    model = Track.artists.through
    extra = 0

class ArtistAdmin(admin.ModelAdmin):
    inlines = [TrackInline,]

class TrackGenreline(admin.StackedInline):
    model = Track.genres.through
    extra = 0

class GenreAdmin(admin.ModelAdmin):
    inlines = [TrackGenreline, ]  

admin.site.register(Album, AlbumAdmin) 
admin.site.register(Track, TrackAdmin) 
admin.site.register(Artist, ArtistAdmin) 
admin.site.register(Genre, GenreAdmin) 
admin.site.register(TrackType)