# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RImagine(RPackage):
	"""IMAGing engINEs, Tools for Application of Image Filters to Data
Matrices

	Provides fast application of image filters to data matrices,
    using R and C++ algorithms.
	"""
	
	homepage = "https://github.com/LuisLauM/imagine"
	cran = "imagine" 

	version("2.1.0", md5="f0f3728a694401e9c9f5c5780619e90a")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
