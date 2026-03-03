# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLeontief(RPackage):
	"""Input-Output Analysis

	An implementation of the Input-Output model developed by
    Wassily Leontief that represents the interdependencies between different 
    sectors of a national economy or different regional economies.
	"""
	
	homepage = "https://pachamaltese.github.io/leontief"
	cran = "leontief" 

	version("0.2", md5="644d93ace715fb9f1b7b9e200210f358")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
