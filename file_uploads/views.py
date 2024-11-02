from django.http import JsonResponse
from django.shortcuts import render
from .forms import UploadFileForm
from .services.encryption_service import EncryptionService
from .services.storage_service import StorageService

import logging

logger = logging.getLogger(__name__)


# Create your views here.


def upload_file(request):
    try:
        if request.method == 'POST':
            form = UploadFileForm(request.POST, request.FILES)
            uploaded_file =  request.FILES['file']
            if not uploaded_file:
                return JsonResponse({'error': 'No file provided'}, status=400)
            
            # Step 2: Generate a new encryption key and encrypt the file
            encryption_key = EncryptionService.generate_key()
            encrypted_content = EncryptionService.encrypt_file(uploaded_file.read(), encryption_key)
            
            # Step 3: Save the encrypted file
            file_name = f"encrypted_{uploaded_file.name}"
            file_url = StorageService.save_file(file_name, encrypted_content)
            # Step 4: Return the encryption key and file URL
            return JsonResponse({
                'message': 'File uploaded and encrypted successfully.',
                'file_url': file_url,
                'encryption_key': encryption_key.decode(),
            })
        else:
            form = UploadFileForm()
            return render(request, 'upload.html', {'form': form})
        
    except FileNotFoundError:
        logger.error("The specified file was not found.")
        # Handle the specific error, e.g., return a specific response
        return JsonResponse({'error': 'The specified file was not found'}, status=400)
    
    except IOError as e:
        return JsonResponse({'error': f"File error: {str(e)}"}, status=500)

    except ValueError:
        logger.error("Invalid data format encountered.")
        return JsonResponse({'error': 'Invalid data format encountered'}, status=400)
    
    except Exception as e:
        logger.exception("Unexpected error during file upload")
        return JsonResponse({'error': 'An error occurred while uploading the file.'}, status=500)