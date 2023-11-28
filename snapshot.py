'''
Take snapshot through microscope's Olympus LC35 camera as the microscope moves through the plate.

Use TWAIN library for cameras.
LC35 should be TWAIN-compliant, as it can be controlled using the DP2-TWAIN software.
Note that TWAIN module can only be downloaded on Windoes devices.

The current Matlab code should take care of the microscope movement.
'''

import twain

def acquire_image():
    # Set up the TWAIN source manager
    sm = twain.SourceManager(0)
    try:
        # Open the default source (scanner/camera)
        source = sm.OpenSource()
        
        # Initiate the scanning process
        source.RequestAcquire(0, 0)
        
        # Get the info about the pending transfers
        info = source.GetImageInfo()
        
        # Actually transfer the image
        image = source.XferImageNatively()
        if image:
            (handle, count) = image
            # Handle the image. This could involve converting it to a different format
            # and saving or processing it as required.

            # Close the image handle
            twain.DIBToBMFile(handle, 'output.bmp')
            twain.GlobalHandleFree(handle)
        else:
            print('No image captured.')
    finally:
        # Clean up the source and source manager
        source.Close()
        sm.Destroy()
    
acquire_image()
