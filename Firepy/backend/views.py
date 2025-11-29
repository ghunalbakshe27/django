from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from backend.models import Song

from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
from backend.models import customuser
User = customuser


# from django.http import HttpResponse
# import sys


# def debug_test(request):
#     """Complete diagnostic test"""
    
#     debug_info = []
    
#     # Test 1: Check if model exists
#     try:
#         from backend.models import Song
#         debug_info.append("✅ Song model imported successfully")
#     except Exception as e:
#         debug_info.append(f"❌ Song model import failed: {str(e)}")
#         return HttpResponse("<br>".join(debug_info))
    
#     # Test 2: Check database connection
#     try:
#         from django.db import connection
#         with connection.cursor() as cursor:
#             cursor.execute("SELECT 1")
#             debug_info.append("✅ Database connection working")
#     except Exception as e:
#         debug_info.append(f"❌ Database connection failed: {str(e)}")
    
#     # Test 3: Check if table exists
#     try:
#         from django.db import connection
#         with connection.cursor() as cursor:
#             cursor.execute("SHOW TABLES LIKE 'backend_song'")
#             result = cursor.fetchone()
#             if result:
#                 debug_info.append("✅ Table 'backend_song' exists in database")
#             else:
#                 debug_info.append("❌ Table 'backend_song' NOT found in database")
#                 debug_info.append("🔧 FIX: Run 'python manage.py migrate'")
#     except Exception as e:
#         debug_info.append(f"❌ Table check failed: {str(e)}")
    
#     # Test 4: Count total songs
#     try:
#         total = Song.objects.all().count()
#         debug_info.append(f"✅ Total songs in database: {total}")
        
#         if total == 0:
#             debug_info.append("⚠️ WARNING: No songs found! Add songs from admin panel")
#     except Exception as e:
#         debug_info.append(f"❌ Failed to count songs: {str(e)}")
    
#     # Test 5: List all songs
#     try:
#         songs = Song.objects.all()[:10]
#         if songs:
#             debug_info.append("<br><strong>📋 Songs in database:</strong>")
#             for i, song in enumerate(songs, 1):
#                 debug_info.append(f"{i}. {song.title} - {song.artist} (Category: {song.category})")
#         else:
#             debug_info.append("📋 No songs to display")
#     except Exception as e:
#         debug_info.append(f"❌ Failed to list songs: {str(e)}")
    
#     # Test 6: Check categories
#     try:
#         from django.db.models import Count
#         categories = Song.objects.values('category').annotate(count=Count('category'))
#         if categories:
#             debug_info.append("<br><strong>📊 Songs by category:</strong>")
#             for cat in categories:
#                 debug_info.append(f"- {cat['category']}: {cat['count']} songs")
#     except Exception as e:
#         debug_info.append(f"❌ Category check failed: {str(e)}")
    
#     # Test 7: Check Arjit songs specifically
#     try:
#         arjit_count = Song.objects.filter(category='arjit').count()
#         debug_info.append(f"<br>✅ Arjit Singh songs: {arjit_count}")
        
#         if arjit_count == 0:
#             debug_info.append("⚠️ No songs with category='arjit'")
#             debug_info.append("🔧 FIX: Add songs with category 'Arjit Singh' from admin")
#     except Exception as e:
#         debug_info.append(f"❌ Arjit songs check failed: {str(e)}")
    
#     # Test 8: Check template path
#     try:
#         import os
#         from django.conf import settings
#         template_path = os.path.join(settings.BASE_DIR, 'backend/templates/backend/arjit.html')
#         if os.path.exists(template_path):
#             debug_info.append("<br>✅ Template file exists: arjit.html")
#         else:
#             debug_info.append("<br>❌ Template file NOT found: arjit.html")
#             debug_info.append(f"🔧 Expected location: {template_path}")
#     except Exception as e:
#         debug_info.append(f"❌ Template check failed: {str(e)}")
    
#     # Test 9: Check media settings
#     try:
#         from django.conf import settings
#         debug_info.append(f"<br>📁 MEDIA_URL: {settings.MEDIA_URL}")
#         debug_info.append(f"📁 MEDIA_ROOT: {settings.MEDIA_ROOT}")
#     except Exception as e:
#         debug_info.append(f"❌ Media settings check failed: {str(e)}")
    
#     # Test 10: Python and Django version
#     try:
#         import django
#         debug_info.append(f"<br>🐍 Python version: {sys.version}")
#         debug_info.append(f"🎯 Django version: {django.get_version()}")
#     except Exception as e:
#         debug_info.append(f"❌ Version check failed: {str(e)}")
    
#     # Generate HTML response
#     html = f"""
#     <!DOCTYPE html>
#     <html>
#     <head>
#         <title>FIREPY Debug Test</title>
#         <style>
#             body {{
#                 font-family: 'Courier New', monospace;
#                 background: #1a1a1a;
#                 color: #0f0;
#                 padding: 40px;
#                 line-height: 1.8;
#             }}
#             h1 {{
#                 color: #ff5733;
#                 border-bottom: 2px solid #ff5733;
#                 padding-bottom: 10px;
#             }}
#             .info {{
#                 background: #000;
#                 padding: 20px;
#                 border-radius: 10px;
#                 border: 1px solid #333;
#                 margin-top: 20px;
#             }}
#             .success {{ color: #0f0; }}
#             .error {{ color: #f00; }}
#             .warning {{ color: #ff0; }}
#         </style>
#     </head>
#     <body>
#         <h1>🔍 FIREPY DEBUG TEST RESULTS</h1>
#         <div class="info">
#             {'<br>'.join(debug_info)}
#         </div>
#         <br>
#         <a href="/arjit-singh/" style="color: #ff5733;">→ Go to Arjit Songs Page</a> | 
#         <a href="/admin/" style="color: #ff5733;">→ Go to Admin Panel</a>
#     </body>
#     </html>
#     """
    
#     return HttpResponse(html)

# def simple_test(request):
#     """Simple test to check if view is working"""
    
#     html = """
#     <!DOCTYPE html>
#     <html>
#     <head>
#         <title>Simple Test</title>
#         <style>
#             body { 
#                 background: black; 
#                 color: white; 
#                 padding: 40px;
#                 font-family: Arial;
#                 text-align: center;
#             }
#             h1 { color: #ff5733; font-size: 48px; }
#             p { font-size: 20px; margin: 20px; }
#             a { 
#                 color: #ff5733; 
#                 text-decoration: none;
#                 border: 2px solid #ff5733;
#                 padding: 15px 30px;
#                 display: inline-block;
#                 margin: 10px;
#                 border-radius: 5px;
#                 transition: all 0.3s;
#             }
#             a:hover {
#                 background: #ff5733;
#                 color: white;
#             }
#         </style>
#     </head>
#     <body>
#         <h1>✅ Django View is Working!</h1>
#         <p>If you can see this, your Django setup is correct.</p>
#         <p>Ab next tests run karo:</p>
#         <a href="/db-test/">Database Test</a>
#         <a href="/debug-test/">Full Debug Test</a>
#         <a href="/admin/">Admin Panel</a>
#     </body>
#     </html>
#     """
    
#     return HttpResponse(html)


# # ========================================
# # TEST VIEW 2: Database Direct Test
# # ========================================

# def db_test(request):
#     """Direct database query test"""
    
#     from django.db import connection
    
#     results = []
    
#     try:
#         with connection.cursor() as cursor:
#             # Test 1: Show all tables
#             cursor.execute("SHOW TABLES")
#             tables = cursor.fetchall()
#             results.append("<h2>📋 All Tables in Database:</h2>")
#             results.append("<ul>")
#             for table in tables:
#                 results.append(f"<li>{table[0]}</li>")
#             results.append("</ul>")
            
#             # Test 2: Check if backend_song exists
#             cursor.execute("SHOW TABLES LIKE 'backend_song'")
#             song_table = cursor.fetchone()
            
#             if song_table:
#                 results.append("<h2 style='color: #0f0;'>✅ backend_song table EXISTS</h2>")
                
#                 # Test 3: Describe table structure
#                 cursor.execute("DESCRIBE backend_song")
#                 columns = cursor.fetchall()
#                 results.append("<h3>Table Structure:</h3>")
#                 results.append("<table border='1' style='border-collapse: collapse; width: 100%;'>")
#                 results.append("<tr><th>Field</th><th>Type</th><th>Null</th><th>Key</th></tr>")
#                 for col in columns:
#                     results.append(f"<tr><td>{col[0]}</td><td>{col[1]}</td><td>{col[2]}</td><td>{col[3]}</td></tr>")
#                 results.append("</table>")
                
#                 # Test 4: Count rows
#                 cursor.execute("SELECT COUNT(*) FROM backend_song")
#                 count = cursor.fetchone()[0]
#                 results.append(f"<h2>Total songs in database: <span style='color: #ff5733;'>{count}</span></h2>")
                
#                 # Test 5: Show all songs
#                 if count > 0:
#                     cursor.execute("SELECT id, title, artist, category, duration FROM backend_song LIMIT 20")
#                     songs = cursor.fetchall()
#                     results.append("<h3>📀 Songs List:</h3>")
#                     results.append("<table border='1' style='border-collapse: collapse; width: 100%;'>")
#                     results.append("<tr><th>ID</th><th>Title</th><th>Artist</th><th>Category</th><th>Duration</th></tr>")
#                     for song in songs:
#                         results.append(f"<tr><td>{song[0]}</td><td>{song[1]}</td><td>{song[2]}</td><td>{song[3]}</td><td>{song[4]}</td></tr>")
#                     results.append("</table>")
                    
#                     # Test 6: Count by category
#                     cursor.execute("SELECT category, COUNT(*) as count FROM backend_song GROUP BY category")
#                     categories = cursor.fetchall()
#                     results.append("<h3>📊 Songs by Category:</h3>")
#                     results.append("<ul>")
#                     for cat in categories:
#                         results.append(f"<li><strong>{cat[0]}</strong>: {cat[1]} songs</li>")
#                     results.append("</ul>")
#                 else:
#                     results.append("<h2 style='color: red;'>⚠️ NO SONGS IN DATABASE!</h2>")
#                     results.append("<p>Fix: Go to <a href='/admin/'>Admin Panel</a> and add songs.</p>")
#             else:
#                 results.append("<h2 style='color: red;'>❌ backend_song table NOT FOUND!</h2>")
#                 results.append("<p style='color: yellow;'>🔧 FIX: Run these commands in terminal:</p>")
#                 results.append("<pre style='background: #333; padding: 20px; border-radius: 5px;'>")
#                 results.append("python manage.py makemigrations\n")
#                 results.append("python manage.py migrate")
#                 results.append("</pre>")
                
#     except Exception as e:
#         results.append(f"<h2 style='color: red;'>❌ ERROR:</h2>")
#         results.append(f"<pre style='background: #333; padding: 20px; color: red;'>{str(e)}</pre>")
    
#     html = f"""
#     <!DOCTYPE html>
#     <html>
#     <head>
#         <title>Database Test</title>
#         <style>
#             body {{ 
#                 background: #1a1a1a; 
#                 color: white; 
#                 padding: 40px; 
#                 font-family: 'Courier New', monospace;
#             }}
#             h1 {{ color: #ff5733; border-bottom: 2px solid #ff5733; padding-bottom: 10px; }}
#             h2 {{ color: #ff5733; margin-top: 30px; }}
#             h3 {{ color: #ffa500; }}
#             table {{ 
#                 margin: 20px 0; 
#                 background: #000;
#             }}
#             th {{ 
#                 background: #ff5733; 
#                 padding: 10px;
#                 color: white;
#             }}
#             td {{ 
#                 padding: 8px; 
#                 border: 1px solid #333;
#             }}
#             pre {{ 
#                 background: #000; 
#                 padding: 15px; 
#                 border-radius: 5px; 
#                 overflow-x: auto;
#             }}
#             code {{ 
#                 background: #333; 
#                 padding: 3px 8px; 
#                 border-radius: 3px; 
#             }}
#             a {{ 
#                 color: #ff5733; 
#                 text-decoration: none;
#             }}
#             a:hover {{ 
#                 text-decoration: underline; 
#             }}
#             ul {{ 
#                 line-height: 2;
#             }}
#         </style>
#     </head>
#     <body>
#         <h1>🗄️ Database Direct Query Test</h1>
#         {''.join(results)}
#         <hr style="margin: 40px 0; border-color: #333;">
#         <p>
#             <a href="/simple-test/">← Simple Test</a> | 
#             <a href="/debug-test/">Full Debug Test →</a> | 
#             <a href="/admin/">Admin Panel</a>
#         </p>
#     </body>
#     </html>
#     """
    
#     return HttpResponse(html)


# # ========================================
# # TEST VIEW 3: Complete Debug Test
# # ========================================

# def debug_test(request):
#     """Complete diagnostic test"""
    
#     debug_info = []
    
#     # Test 1: Check if model exists
#     try:
#         from backend.models import Song
#         debug_info.append("✅ Song model imported successfully")
#     except Exception as e:
#         debug_info.append(f"❌ Song model import failed: {str(e)}")
#         return HttpResponse("<br>".join(debug_info))
    
#     # Test 2: Check database connection
#     try:
#         from django.db import connection
#         with connection.cursor() as cursor:
#             cursor.execute("SELECT 1")
#             debug_info.append("✅ Database connection working")
#     except Exception as e:
#         debug_info.append(f"❌ Database connection failed: {str(e)}")
    
#     # Test 3: Check if table exists
#     try:
#         from django.db import connection
#         with connection.cursor() as cursor:
#             cursor.execute("SHOW TABLES LIKE 'backend_song'")
#             result = cursor.fetchone()
#             if result:
#                 debug_info.append("✅ Table 'backend_song' exists in database")
#             else:
#                 debug_info.append("❌ Table 'backend_song' NOT found in database")
#                 debug_info.append("🔧 FIX: Run 'python manage.py migrate'")
#     except Exception as e:
#         debug_info.append(f"❌ Table check failed: {str(e)}")
    
#     # Test 4: Count total songs
#     try:
#         total = Song.objects.all().count()
#         debug_info.append(f"✅ Total songs in database: <strong style='color: #ff5733;'>{total}</strong>")
        
#         if total == 0:
#             debug_info.append("⚠️ WARNING: No songs found! Add songs from admin panel")
#     except Exception as e:
#         debug_info.append(f"❌ Failed to count songs: {str(e)}")
    
#     # Test 5: List all songs
#     try:
#         songs = Song.objects.all()[:10]
#         if songs:
#             debug_info.append("<br><strong>📋 Songs in database:</strong><ul>")
#             for i, song in enumerate(songs, 1):
#                 debug_info.append(f"<li>{i}. <strong>{song.title}</strong> - {song.artist} (Category: <em>{song.category}</em>)</li>")
#             debug_info.append("</ul>")
#         else:
#             debug_info.append("📋 No songs to display")
#     except Exception as e:
#         debug_info.append(f"❌ Failed to list songs: {str(e)}")
    
#     # Test 6: Check categories
#     try:
#         from django.db.models import Count
#         categories = Song.objects.values('category').annotate(count=Count('category'))
#         if categories:
#             debug_info.append("<br><strong>📊 Songs by category:</strong><ul>")
#             for cat in categories:
#                 debug_info.append(f"<li><strong>{cat['category']}</strong>: {cat['count']} songs</li>")
#             debug_info.append("</ul>")
#     except Exception as e:
#         debug_info.append(f"❌ Category check failed: {str(e)}")
    
#     # Test 7: Check Arjit songs specifically
#     try:
#         arjit_count = Song.objects.filter(category='arjit').count()
#         debug_info.append(f"<br>🎤 Arjit Singh songs: <strong style='color: #ff5733;'>{arjit_count}</strong>")
        
#         if arjit_count == 0:
#             debug_info.append("⚠️ No songs with category='arjit'")
#             debug_info.append("🔧 FIX: Add songs with category 'Arjit Singh' from admin")
#         else:
#             arjit_songs = Song.objects.filter(category='arjit')[:5]
#             debug_info.append("<ul>")
#             for song in arjit_songs:
#                 debug_info.append(f"<li>{song.title}</li>")
#             debug_info.append("</ul>")
#     except Exception as e:
#         debug_info.append(f"❌ Arjit songs check failed: {str(e)}")
    
#     # Test 8: Check template path
#     try:
#         import os
#         from django.conf import settings
#         template_path = os.path.join(settings.BASE_DIR, 'backend/templates/backend/arjit.html')
#         if os.path.exists(template_path):
#             debug_info.append("<br>✅ Template file exists: arjit.html")
#         else:
#             debug_info.append("<br>❌ Template file NOT found: arjit.html")
#             debug_info.append(f"🔧 Expected location: <code>{template_path}</code>")
#     except Exception as e:
#         debug_info.append(f"❌ Template check failed: {str(e)}")
    
#     # Test 9: Check media settings
#     try:
#         from django.conf import settings
#         debug_info.append(f"<br>📁 MEDIA_URL: <code>{settings.MEDIA_URL}</code>")
#         debug_info.append(f"📁 MEDIA_ROOT: <code>{settings.MEDIA_ROOT}</code>")
#     except Exception as e:
#         debug_info.append(f"❌ Media settings check failed: {str(e)}")
    
#     # Test 10: Python and Django version
#     try:
#         import django
#         debug_info.append(f"<br>🐍 Python version: <code>{sys.version.split()[0]}</code>")
#         debug_info.append(f"🎯 Django version: <code>{django.get_version()}</code>")
#     except Exception as e:
#         debug_info.append(f"❌ Version check failed: {str(e)}")
    
#     # Generate HTML response
#     html = f"""
#     <!DOCTYPE html>
#     <html>
#     <head>
#         <title>FIREPY Debug Test</title>
#         <style>
#             body {{
#                 font-family: 'Courier New', monospace;
#                 background: #1a1a1a;
#                 color: #0f0;
#                 padding: 40px;
#                 line-height: 1.8;
#             }}
#             h1 {{
#                 color: #ff5733;
#                 border-bottom: 2px solid #ff5733;
#                 padding-bottom: 10px;
#             }}
#             .info {{
#                 background: #000;
#                 padding: 20px;
#                 border-radius: 10px;
#                 border: 1px solid #333;
#                 margin-top: 20px;
#             }}
#             .success {{ color: #0f0; }}
#             .error {{ color: #f00; }}
#             .warning {{ color: #ff0; }}
#             code {{
#                 background: #333;
#                 padding: 2px 6px;
#                 border-radius: 3px;
#                 color: #ff5733;
#             }}
#             ul {{
#                 margin: 10px 0;
#                 padding-left: 20px;
#             }}
#             li {{
#                 margin: 5px 0;
#             }}
#             a {{
#                 color: #ff5733;
#                 text-decoration: none;
#                 margin: 0 10px;
#             }}
#             a:hover {{
#                 text-decoration: underline;
#             }}
#         </style>
#     </head>
#     <body>
#         <h1>🔍 FIREPY DEBUG TEST RESULTS</h1>
#         <div class="info">
#             {'<br>'.join(debug_info)}
#         </div>
#         <br>
#         <hr style="border-color: #333;">
#         <p style="margin-top: 20px;">
#             <a href="/simple-test/">Simple Test</a> | 
#             <a href="/db-test/">Database Test</a> | 
#             <a href="/arjit-singh/">Arjit Songs Page</a> | 
#             <a href="/admin/">Admin Panel</a>
#         </p>
#     </body>
#     </html>
#     """
    
#     return HttpResponse(html)

def aboutus(request):
    return render(request, 'backend/aboutus.html')

def arjit(request):
    return render(request, 'backend/arjit.html')

def bhajan(request):
    return render(request, 'backend/bhajan.html')

def drivelist(request):
    return render(request, 'backend/drivelist.html')

def genres(request):
    return render(request, 'backend/genres.html')

def honeys(request):
    return render(request, 'backend/honeys.html')

def indianhits(request):
    return render(request, 'backend/indianhits.html')

def mixlist(request):
    return render(request, 'backend/mixlist.html')

def new_releases(request):
     # Get all songs with category 'new_release', ordered by newest first
    new_release_songs = Song.objects.filter(category='new_releases').order_by('-release_date')[:12]
    
    context = {
        'songs': new_release_songs
    }
    return render(request, 'backend/new_releases.html', context)
    # return render(request, 'backend/new releases.html')
def phonk(request):
    return render(request, 'backend/phonk.html')

def punjabi_hits(request):
    return render(request, 'backend/punjabi hits.html')

def subh1(request):
    return render(request, 'backend/subh1.html')

def top(request):
    return render(request, 'backend/top.html')

def topeng(request):
    return render(request, 'backend/topeng.html')

def trend(request):
    return render(request, 'backend/trend.html')


@csrf_protect
def user_login(request):
    # """Handle user login"""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Authenticate user
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, 'You have been logged out successfully!')
            return redirect('homepage')
        else:
            messages.error(request, 'Invalid username or password!')
            return render(request, 'backend/index.html')
    
    return render(request, 'backend/index.html')

@csrf_protect
def user_register(request):
    # """Handle user registration"""
    if request.method == 'POST':
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirmpassword')
        
        # Split fullname into first_name and last_name
        name_parts = fullname.strip().split(' ', 1)  # Split only on first space
        first_name = name_parts[0] if name_parts else ''
        last_name = name_parts[1] if len(name_parts) > 1 else ''
        
        # Basic validation
        if not fullname.strip():
            messages.error(request, 'Full name is required!')
            return redirect('ogregister')
            
        if password != confirm_password:
            messages.error(request, 'Passwords do not match!')
            return redirect('ogregister')
        
        # Check if username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists!')
            return redirect('ogregister')
        
        # Check if email already exists
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists!')
            return redirect('ogregister')
        
        try:
            # Create new user - THIS SAVES TO YOUR MYSQL DATABASE! 🔥
            user = User.objects.create_user(
                username=username,
                email=email,
                first_name=first_name,
                last_name=last_name
            )
            user.set_password(password)  # Hash the password
            user.save()
            
            messages.success(request, 'Registration successful! Please login with your credentials.')
            return redirect('user_login')
            
        except Exception as e:
            messages.error(request, 'Registration failed. Please try again.')
            return redirect('ogregister')
    return render(request, 'backend/ogregister.html')


def user_logout(request):
    # """Handle user logout"""
    logout(request)
    messages.success(request, 'You have been logged out successfully!')
    return redirect('user_login')

def homepage(request):
    if not request.user.is_authenticated:
        return redirect('user_login')
    return render(request, 'backend/homepage.html')
