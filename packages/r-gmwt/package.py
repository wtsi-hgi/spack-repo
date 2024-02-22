# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGmwt(RPackage):
	"""Generalized Mann-Whitney Type Tests

	Generalized Mann-Whitney type tests based on probabilistic
        indices and new diagnostic plots, for the underlying manuscript see Fischer, Oja (2015) <doi:10.18637/jss.v065.i09>.
	"""
	
	cran = "gMWT" 

	version("1.4", md5="7896f2e19d3b2fe293cabd291f19fbe6")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-clinfun", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
