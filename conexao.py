
from supabase import create_client

url = "https://ghrzodhebrxgpxkdfznn.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImdocnpvZGhlYnJ4Z3B4a2Rmem5uIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzM0MzM5NTUsImV4cCI6MjA4OTAwOTk1NX0.fn_PqkHWNYQGuLR6WUOqoPXXpopUi1nuVPLklfECRoo"

supabase = create_client(url, key)