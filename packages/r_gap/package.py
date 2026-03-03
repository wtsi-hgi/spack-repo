# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGap(RPackage):
	"""Genetic Analysis Package

	As first reported [Zhao, J. H. 2007. "gap: Genetic Analysis Package". J Stat Soft 23(8):1-18.
        <doi:10.18637/jss.v023.i08>], it is designed as an integrated package for genetic data
        analysis of both population and family data. Currently, it contains functions for
        sample size calculations of both population-based and family-based designs, probability
        of familial disease aggregation, kinship calculation, statistics in linkage analysis,
        and association analysis involving genetic markers including haplotype analysis with or
        without environmental covariates. Over years, the package has been developed in-between
        many projects hence also in line with the name (gap).
	"""
	
	homepage = "https://github.com/jinghuazhao/R"
	cran = "gap" 

	version("1.5-3", md5="69266dcc6a164090d5c0c9a22b3b839e")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-gap-datasets@0.0.6:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
