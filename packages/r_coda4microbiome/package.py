# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCoda4microbiome(RPackage):
	"""Compositional Data Analysis for Microbiome Studies

	Functions for microbiome data analysis that take into account its compositional nature. Performs variable selection through penalized regression for both, cross-sectional and longitudinal studies, and for binary and continuous outcomes.    
	"""
	
	homepage = "https://malucalle.github.io/coda4microbiome/"
	cran = "coda4microbiome" 

	version("0.2.3", md5="0af10e436d1d96a4b09d266454ecaedc")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-corrplot", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-proc", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-complexheatmap", type=("build", "run"))
	depends_on("r-circlize", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-survminer", type=("build", "run"))
