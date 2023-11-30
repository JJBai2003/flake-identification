%% CONNECTING AND INITIALIZING DEVICES
NET.addAssembly('C:\Program Files\Thorlabs\Kinesis\Thorlabs.MotionControl.DeviceManagerCLI.dll');
NET.addAssembly('C:\Program Files\Thorlabs\Kinesis\Thorlabs.MotionControl.GenericMotorCLI.dll');
NET.addAssembly('C:\Program Files\Thorlabs\Kinesis\Thorlabs.MotionControl.KCube.DCServoCLI.dll');
%Initialize Device List
import Thorlabs.MotionControl.DeviceManagerCLI.*
import Thorlabs.MotionControl.GenericMotorCLI.*
import Thorlabs.MotionControl.KCube.DCServoCLI.*
%Initialize Device List
DeviceManagerCLI.BuildDeviceList()
DeviceManagerCLI.GetDeviceListSize()
SLnoList= Thorlabs.MotionControl.DeviceManagerCLI.DeviceManagerCLI.GetDeviceList()
serialNumbers=cell(ToArray(SLnoList))
%Should change the serial number below to the one being used.
serial_numX=serialNumbers{2};
serial_numY=serialNumbers{1};
timeout_val=60000;
%Set up device and configuration
KDC101X = KCubeDCServo.CreateKCubeDCServo(serial_numX);
KDC101X.Connect(serial_numX);
KDC101X.WaitForSettingsInitialized(5000);
% configure the stage
motorSettings = KDC101X.LoadMotorConfiguration(serial_numX);
motorSettings.DeviceSettingsName = 'MTS50-Z8';
% update the RealToDeviceUnit converter
motorSettings.UpdateCurrentConfiguration();
% push the settings down to the device
MotorDeviceSettings = KDC101X.MotorDeviceSettings;
KDC101X.SetSettings(MotorDeviceSettings, true, false);
KDC101X.StartPolling(250);
%Set up device and configuration
KDC101Y = KCubeDCServo.CreateKCubeDCServo(serial_numY);
KDC101Y.Connect(serial_numY);
KDC101Y.WaitForSettingsInitialized(5000);
% configure the stage
motorSettings = KDC101Y.LoadMotorConfiguration(serial_numY);
motorSettings.DeviceSettingsName = 'MTS50-Z8';
% update the RealToDeviceUnit converter
motorSettings.UpdateCurrentConfiguration();
% push the settings down to the device
MotorDeviceSettings = KDC101Y.MotorDeviceSettings;
KDC101Y.SetSettings(MotorDeviceSettings, true, false);
KDC101Y.StartPolling(250);
pause(1); %wait to make sure device is enabled
dir = Thorlabs.MotionControl.GenericMotorCLI.MotorDirection;
%raster scan using KDC101.MoveRelative commands and taking image
% KDC101home(KDC101X,timeout_val);
% KDC101home(KDC101Y,timeout_val)
%KDC101moveto(KDC101X,  4.7993,timeout_val);
% KDC101moveto(KDC101Y, 27.350,timeout_val);
%KDC101X.MoveRelative(dir, 1, timeout_val);
%KDC101Y.MoveRelative(dir, 0.3, timeout_val);
%posy = System.Decimal.ToDouble(KDC101Y.Position)
% %pause(2);
%     KDC101X.MoveTo(33.156690+0.063,timeout_val);
%     KDC101Y.MoveTo(38.577700+0.091,timeout_val);
%   KDC101X.MoveRelative(dir, 1.00 , timeout_val);
%   KDC101Y.MoveRelative(dir, 0.260, timeout_val);   
%pause(3);

