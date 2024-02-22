# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RImagerextra(RPackage):
	"""Extra Image Processing Library Based on 'imager'

	Provides advanced functions for image processing based on the package 'imager'.
	"""
	
	homepage = "https://github.com/ShotaOchi/imagerExtra"
	cran = "imagerExtra" 

	version("1.3.2", md5="30048d65d29551edf8bdeb4805844f8b")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-imager@0.40.2:", type=("build", "run"))
	depends_on("r-fftwtools", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
