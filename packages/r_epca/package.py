# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REpca(RPackage):
	"""Exploratory Principal Component Analysis

	
    Exploratory principal component analysis for large-scale dataset, including sparse principal component analysis and sparse matrix approximation.
	"""
	
	homepage = "https://github.com/fchen365/epca"
	cran = "epca" 

	version("1.1.0", md5="9405d716fcdaa707f9f40d9356e6a171")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-clue", type=("build", "run"))
	depends_on("r-irlba", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-gparotation", type=("build", "run"))
