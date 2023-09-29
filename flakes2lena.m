originalflakes = imread('testflake.tif');
originalflakesgray = rgb2gray(originalflakes);
BW = imbinarize(originalflakesgray);

%Figure 1: outlining all flakes 
[B,L,N] = bwboundaries(BW, 'noholes');
Fig = figure;
%imshow(label2rgb(L,@jet, [0.5,0.5,0.5]));
subplot(2,2,1);
imshow(originalflakes); 
hold on
for k = 1:length(B)
    boundary = B{k};
    plot(boundary(:,2), boundary(:,1), 'c', 'LineWidth', 2)
end 

%Figure 2: finding centroids of all flake pieces
%areas are set to remove any residue or dirt pieces picked up
flakearea = bwarea(BW);
subplot(2,2,2);
%both of these work just need to change the 300 or 500 depending on what
%flake size we want to start with 
%BW2 = bwareafilt(BW,[500 50000]);
BW2 = bwareaopen(BW,300);
s = regionprops("table", BW2, 'centroid', 'area');
centroids = cat(1,s.Centroid);
imshow(BW2)
hold on
plot(centroids(:,1),centroids(:,2),'m*');

% %Figure 3: Histogram of Areas
% areastats = regionprops("table", BW2, 'centroid', 'area')
% %areas = areastats.area
% subplot(2,2,3);
% areahistogram = histogram(areastats.Area)
% %plot(areahistogram);

%Figure 4: Colored outlines of good and bad flakes based on areas  
subplot(2,2,4);
%can change out the areafilt ranges once dimensions are known
BW3 = bwareafilt(BW,[0 2000]);
BW4 = bwareafilt(BW, [2000 500000]);
[B3,L3,N3] = bwboundaries(BW3, 'noholes');
[B4,L4,N4] = bwboundaries(BW4, 'noholes');
imshow(originalflakes);
hold on
for k = 1:length(B3)
    boundary = B3{k};
    plot(boundary(:,2), boundary(:,1), 'r', 'LineWidth', 2)
end 
for k = 1:length(B4)
    boundary = B4{k};
    plot(boundary(:,2), boundary(:,1), 'g', 'LineWidth', 2)
end 

saveas(Fig, 'endflakes.png');
