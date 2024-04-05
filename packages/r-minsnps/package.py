# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMinsnps(RPackage):
	"""Resolution-Optimised SNPs Searcher

	This is a R implementation of "Minimum SNPs" software as described in "Price E.P., Inman-Bamber, J., Thiruvenkataswamy, V., Huygens, F and Giffard, P.M." (2007) <doi:10.1186/1471-2105-8-278> "Computer-aided identification of polymorphism sets diagnostic for groups of bacterial and viral genetic variants."
	"""
	
	homepage = "https://github.com/ludwigHoon/minSNPs"
	cran = "minSNPs" 

	version("0.2.0", md5="6236eed5178bb53b695144b82a5a0cb9")
	version("0.1.0", md5="4d3f6cd934761e397d2006700de757be")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
