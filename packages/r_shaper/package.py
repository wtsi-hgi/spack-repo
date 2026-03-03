# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShaper(RPackage):
	"""Collection and Analysis of Otolith Shape Data

	Studies otolith shape variation among fish populations.
  Otoliths are calcified structures found in the inner ear of teleost fish and their shape has
  been known to vary among several fish populations and stocks, making them very useful in taxonomy,
  species identification and to study geographic variations. The package extends previously described
  software used for otolith shape analysis by allowing the user to automatically extract closed
  contour outlines from a large number of images, perform smoothing to eliminate pixel noise described in Haines and Crampton (2000) <doi:10.1111/1475-4983.00148>,
  choose from conducting either a Fourier or wavelet see Gençay et al (2001) <doi:10.1016/S0378-4371(00)00463-5> transform to the outlines and visualize
  the mean shape. The output of the package are independent Fourier or wavelet coefficients
  which can be directly imported into a wide range of statistical packages in R. The package
  might prove useful in studies of any two dimensional objects.
	"""
	
	homepage = "https://github.com/lisalibungan/shapeR"
	cran = "shapeR" 

	version("1.0-1", md5="015a7cc2ce4b3c7d13307bbcdc63c88f")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-plotrix", type=("build", "run"))
	depends_on("r-jpeg", type=("build", "run"))
	depends_on("r-pixmap", type=("build", "run"))
	depends_on("r-wavethresh", type=("build", "run"))
	depends_on("r-vegan", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
