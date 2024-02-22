# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFacerec(RPackage):
	"""An Interface for Face Recognition

	Provides an interface to the 'Kairos' Face Recognition API <https://kairos.com/face-recognition-api>. The API detects faces in images and returns estimates for demographics like gender, ethnicity and age.  
	"""
	
	homepage = "https://github.com/methodds/facerec"
	cran = "facerec" 

	version("0.1.0", md5="c2aae46e70aad06751677849d22791ff")

	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-dplyr@0.7:", type=("build", "run"))
	depends_on("r-httr@1.3:", type=("build", "run"))
	depends_on("r-jsonlite@1.5:", type=("build", "run"))
	depends_on("r-knitr@1.2:", type=("build", "run"))
	depends_on("r-stringr@1.2:", type=("build", "run"))
	depends_on("r-snakecase@0.9:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
