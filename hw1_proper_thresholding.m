image = imread('einstein512_512c.jpg');

bwImage = rgb2gray(image);
figure;
imshow(bwImage);
title('bw image');

%size of bw image
[r, c] = size(bwImage);

%average value of the pixels
average = mean(mean(bwImage));
newAverage = 0;

lowerPixels = zeros(r,c);
higherPixels = zeros(r,c);

while abs(average - newAverage) > 1
    if newAverage ~= 0
        average = newAverage;
    end
    
    for i = 1 : r
        for j = 1 : c
          if bwImage(i,j) < average
              lowerPixels(i,j) = bwImage(i,j);
          else
              higherPixels(i,j) = bwImage(i,j);
          end
        end
    end

    %averageLower = mean(mean(lowerPixels));
    %averageHigher = mean(mean(higherPixels));
    
    sumLower = 0;
    sumHigher = 0;
    countLower = 0;
    countHigher = 0;
    for i = 1:r
        for j=1:c
            if lowerPixels(i,j) ~= 0
                sumLower  = sumLower + lowerPixels(i,j);
                countLower = countLower + 1;
            end
            if higherPixels(i,j) ~= 0
                sumHigher  = sumHigher + higherPixels(i,j);
                countHigher = countHigher + 1;
            end
        end
    end
    
    averageLower=  sumLower/countLower;
    averageHigher = sumHigher/countHigher;
    
    newAverage =  (averageLower + averageHigher)/2;
    
    lowerPixels = zeros(r,c);
    higherPixels = zeros(r,c);
end

for i = 1 : r
    for j = 1 : c
        if bwImage(i,j) < newAverage
            bwImage(i,j) = 0;
        else
            bwImage(i,j) = 255;
        end
    end
end

figure;
imshow(bwImage);
title('binarized image');