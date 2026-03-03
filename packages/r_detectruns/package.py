# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDetectruns(RPackage):
	"""Detect Runs of Homozygosity and Runs of Heterozygosity in
Diploid Genomes

	Detection of runs of homozygosity and of heterozygosity
    in diploid genomes using two methods: sliding windows (Purcell et al (2007)
    <doi:10.1086/519795>) and consecutive runs (Marras et al (2015)
    <doi:10.1111/age.12259>).
	"""
	
	homepage = "https://github.com/bioinformatics-ptp/detectRUNS/tree/master/detectRUNS"
	cran = "detectRUNS" 

	version("0.9.6", md5="6c859b5efea2a6e8f1a40283abbe53c4")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-iterators", type=("build", "run"))
	depends_on("r-itertools", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
