# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHillr(RPackage):
	"""Diversity Through Hill Numbers

	Calculate taxonomic, functional and phylogenetic diversity measures 
    through Hill Numbers proposed by Chao, Chiu and Jost (2014) 
    <doi:10.1146/annurev-ecolsys-120213-091540>.
	"""
	
	homepage = "https://github.com/daijiang/hillR"
	cran = "hillR" 

	version("0.5.2", md5="53f3db745a70e22e410e05aba05a8d1a")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-fd", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-ade4", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-geiger", type=("build", "run"))
