# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMp(RPackage):
	"""Multidimensional Projection Techniques

	Multidimensional projection techniques are used to create two
    dimensional representations of multidimensional data sets.
	"""
	
	cran = "mp" 

	version("0.4.1", md5="61f2aa7b8bf304bd0843a90e581927fc")

	depends_on("r@1.8:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
