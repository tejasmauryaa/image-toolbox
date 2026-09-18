# image-toolbox
allows user to upload a PNG OR JPG image and apply different geometric transformations to itt using a simple interactive menu. the transformations are based on 2d coordinate transformations and transformation matrix 

The toolbox provides the following options:

**Rotate** – Rotates the image by a user-defined angle.
**Resize** – Enlarges or reduces the image using a scale factor.
**Flip** – Flips the image horizontally or vertically.
**Shear** – Applies horizontal shearing using a user-defined shear factor.
**Custom Matrix** – Allows the user to enter their own 2 × 2 transformation matrix.
**Reset** – Restores the image to its original state.

each pixel in the image is treated as a 2d coordinate, the origin is considered to be at the centre of the image. a transformation matrix is then applied to the coordinates 

For a general transformation matrix:

    [ x' ]   [ a  b ] [ x ]
    [ y' ] = [ c  d ] [ y ]

The new coordinates are calculated as:

    x' = ax + by
    y' = cx + dy

The transformed coordinates are then converted back into image coordinates and the corresponding pixels are placed in their new positions.
