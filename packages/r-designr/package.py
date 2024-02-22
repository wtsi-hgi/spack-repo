# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDesignr(RPackage):
	"""Balanced Factorial Designs

	Generate balanced factorial designs with crossed and nested random and fixed effects <https://github.com/mmrabe/designr>.
	"""
	
	homepage = "https://maxrabe.com/designr"
	cran = "designr" 

	version("0.1.13", md5="c575d001e528e0e96b0065e1278d8724")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-crossdes", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
