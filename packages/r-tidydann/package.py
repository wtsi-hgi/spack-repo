# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTidydann(RPackage):
	"""Add the 'dann' Model and the 'sub_dann' Model to the Tidymodels
Ecosystem

	Provides model specifications, tuning parameters for models in 
    'dann' package. Models based on Hastie (1996) 
    <https://web.stanford.edu/~hastie/Papers/dann_IEEE.pdf>.
	"""
	
	cran = "tidydann" 

	version("1.0.0", md5="6ee3a783042e96e9071987c30f31d008")

	depends_on("r-dials", type=("build", "run"))
	depends_on("r-generics", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-parsnip", type=("build", "run"))
