# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMotif(RPackage):
	"""Local Pattern Analysis

	Describes spatial patterns of categorical raster data for 
    any defined regular and irregular areas. 
    Patterns are described quantitatively using built-in signatures 
    based on co-occurrence matrices but also allows for 
    any user-defined functions. 
    It enables spatial analysis such as search, change detection,
    and clustering to be performed on spatial patterns (Nowosad (2021) <doi:10.1007/s10980-020-01135-0>).
	"""
	
	homepage = "https://jakubnowosad.com/motif/"
	cran = "motif" 

	version("0.6.4", md5="eb6afdcecdf4cadf07bd589277f1e6e3")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-comat@0.7:", type=("build", "run"))
	depends_on("r-philentropy@0.6:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-stars", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
