# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQtl2pattern(RPackage):
	"""Pattern Support for 'qtl2' Package

	Routines in 'qtl2' to study allele patterns in quantitative trait loci (QTL)
    mapping over a chromosome.
    Useful in crosses with more than two alleles to identify how sets of alleles,
    genetically different strands at the same locus, have different response levels.
    Plots show profiles over a chromosome.
    Can handle multiple traits together.
    See <https://github.com/byandell/qtl2pattern>.
	"""
	
	homepage = "https://github.com/byandell/qtl2pattern"
	cran = "qtl2pattern" 

	version("1.2.1", md5="f02dba8b664e091524354ed8f38060d9")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-qtl2", type=("build", "run"))
	depends_on("r-qtl2fst", type=("build", "run"))
	depends_on("r-fst", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
