# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCophescan(RPackage):
	"""Adaptation of the Coloc Method for PheWAS

	
     A Bayesian method for Phenome-wide association studies (PheWAS) that identifies causal associations between genetic variants and traits, while simultaneously addressing confounding due to linkage disequilibrium. For details see   
     Manipur et al (2023) <doi:10.1101/2023.06.29.546856>.
	"""
	
	homepage = "https://github.com/ichcha-m/cophescan"
	cran = "cophescan" 

	version("1.4.0", md5="4436ea16d6142758052bd0b4f6c73586")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-coloc", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-pheatmap", type=("build", "run"))
	depends_on("r-viridis", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
