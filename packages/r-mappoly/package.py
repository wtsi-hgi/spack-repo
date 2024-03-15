# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMappoly(RPackage):
	"""Genetic Linkage Maps in Autopolyploids

	Construction of genetic maps in autopolyploid full-sib populations. 
             Uses pairwise recombination fraction estimation as the first 
             source of information to sequentially position allelic variants 
             in specific homologous chromosomes. For situations where pairwise 
             analysis has limited power, the algorithm relies on the multilocus 
             likelihood obtained through a hidden Markov model (HMM). 
             For more detail, please see  Mollinari and Garcia (2019) 
             <doi:10.1534/g3.119.400378> and Mollinari et al. (2020) 
             <doi:10.1534/g3.119.400620>.
	"""
	
	homepage = "https://github.com/mmollina/MAPpoly"
	cran = "mappoly" 

	version("0.4.1", md5="53455904c3be0c7c5f114da344de259b")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppparallel", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
	depends_on("r-fields", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-ggsci", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
	depends_on("r-plot3d", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-smacof", type=("build", "run"))
	depends_on("r-princurve", type=("build", "run"))
	depends_on("r-dendextend", type=("build", "run"))
	depends_on("r-vcfr", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
