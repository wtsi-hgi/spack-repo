# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRecolorize(RPackage):
	"""Color-Based Image Segmentation

	Automatic, semi-automatic, and manual functions for
    generating color maps from images. The idea is to simplify
    the colors of an image according to a metric that is useful for
    the user, using deterministic methods whenever possible.
    Many images will be clustered well using the out-of-the-box
    functions, but the package also includes a toolbox of functions
    for making manual adjustments (layer merging/isolation, blurring,
    fitting to provided color clusters or those from another image, etc).
    Also includes export methods for other color/pattern analysis packages
    (pavo, patternize, colordistance).
	"""
	
	cran = "recolorize" 

	version("0.1.0", md5="71f404d32a11cf919b7dd09e6d55f5df")

	depends_on("r@3.50:", type=("build", "run"))
	depends_on("r-imager", type=("build", "run"))
	depends_on("r-png", type=("build", "run"))
	depends_on("r-pavo", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-colorramps", type=("build", "run"))
	depends_on("r-plotfunctions", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-plot3d", type=("build", "run"))
