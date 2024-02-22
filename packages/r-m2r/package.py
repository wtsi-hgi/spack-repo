# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RM2r(RPackage):
	"""Interface to 'Macaulay2'

	Persistent interface to 'Macaulay2' <http://www.math.uiuc.edu/Macaulay2/>
    and front-end tools facilitating its use in the 'R' ecosystem. For details see 
    Kahle et. al. (2020) <doi:10.18637/jss.v093.i09>.
	"""
	
	homepage = "https://github.com/coneill-math/m2r"
	cran = "m2r" 

	version("1.0.2", md5="ed5ed2c006feafb0ab3c9dd733690dab")

	depends_on("r-mpoly@1.0.5:", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-memoise", type=("build", "run"))
	depends_on("r-gmp", type=("build", "run"))
	depends_on("r-usethis", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
