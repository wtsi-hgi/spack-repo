# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REpm(RPackage):
	"""EcoPhyloMapper

	Facilitates the aggregation of species' geographic ranges from vector or raster spatial data, and that enables the calculation of various morphological and phylogenetic community metrics across geography. Citation: Title, PO, DL Swiderski and ML Zelditch (2022) <doi:10.1111/2041-210X.13914>. 
	"""
	
	homepage = "https://github.com/ptitle/epm"
	cran = "epm" 

	version("1.1.2", md5="0c05616cee2f0088f29fd1bca4cc4eaf")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-terra@1.5.21:", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-viridislite", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppprogress", type=("build", "run"))
