# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBayefdr(RPackage):
	"""Bayesian Estimation and Optimisation of Expected False Discovery
Rate

	
    Implements the Bayesian FDR control described by 
    Newton et al. (2004), <doi:10.1093/biostatistics/5.2.155>.
    Allows optimisation and visualisation of expected error rates based on
    tail posterior probability tests.
    Based on code written by Catalina Vallejos for BASiCS, see
    Beyond comparisons of means: understanding changes in gene expression at the
    single-cell level Vallejos et al. (2016) <doi:10.1186/s13059-016-0930-3>.
	"""
	
	homepage = "https://github.com/VallejosGroup/bayefdr"
	cran = "bayefdr" 

	version("0.2.1", md5="cb9a9bd3851a7d6e2c86080534b4c555")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-ggextra", type=("build", "run"))
