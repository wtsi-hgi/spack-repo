# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRadstackshelpr(RPackage):
	"""Optimize the De Novo Stacks Pipeline via R

	Offers a handful of useful wrapper functions which streamline
    the reading, analyzing, and visualizing of variant call format (vcf) files in R.
    This package was designed to facilitate an explicit pipeline for optimizing
    Stacks (Rochette et al., 2019) (<doi:10.1111/mec.15253>)
    parameters during de novo (without a reference genome) assembly and variant
    calling of restriction-enzyme associated DNA sequence (RADseq) data. The
    pipeline implemented here is based on the 2017 paper "Lost in Parameter Space"
    (Paris et al., 2017) (<doi:10.1111/2041-210X.12775>) which
    establishes clear recommendations for optimizing the parameters
    'm', 'M', and 'n', during the process of assembling loci.
	"""
	
	cran = "RADstackshelpR" 

	version("0.1.0", md5="2c3cfee83fd679464375125ab6a3f29f")

	depends_on("r-vcfr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggridges", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
