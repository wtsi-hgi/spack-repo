# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPolymapr(RPackage):
	"""Linkage Analysis in Outcrossing Polyploids

	Creation of linkage maps in polyploid species from marker dosage
    scores of an F1 cross from two heterozygous parents. Currently works for outcrossing diploid, autotriploid, autotetraploid and autohexaploid species, 
    as well as segmental allotetraploids. Methods are described in a manuscript of Bourke et al. (2018) <doi:10.1093/bioinformatics/bty371>. Since version 1.1.0,
    both discrete and probabilistic genotypes are acceptable input; for more details on the latter see Liao et al. (2021) <doi:10.1007/s00122-021-03834-x>.
	"""
	
	cran = "polymapR" 

	version("1.1.5", md5="c8a12a97e1492fc0110726447f7d21fd")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-mdsmap", type=("build", "run"))
