# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNda(RPackage):
	"""Generalized Network-Based Dimensionality Reduction and Analysis

	Non-parametric dimensionality reduction function. Reduction with and without feature selection. Plot functions. Automated feature selections. Kosztyan et. al. (2022) <doi:10.1016/j.knosys.2022.109180>.
	"""
	
	homepage = "https://github.com/kzst/nda"
	cran = "nda" 

	version("0.1.13", md5="0d42215c05ea72e878821c82ffd996d1")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-energy", type=("build", "run"))
	depends_on("r-psych", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-ppcor", type=("build", "run"))
	depends_on("r-visnetwork", type=("build", "run"))
