# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcm(RPackage):
	"""Fit row-column association models with the negative binomial distribution for the microbiome

	Combine ideas of log-linear analysis of contingency table, flexible response function estimation and empirical Bayes dispersion estimation for explorative visualization of microbiome datasets. The package includes unconstrained as well as constrained analysis. In addition, diagnostic plot to detect lack of fit are available.
	"""
	
	homepage = "https://bioconductor.org/packages/release/bioc/vignettes/RCM/inst/doc/RCMvignette.html/"
	bioc = "RCM" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/RCM_1.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/RCM/RCM_1.18.0.tar.gz"]

	version("1.18.0", sha256="3b7bfaca7b1e134ee65a09680305f0b4562c8488ad85dfd1d4de94ed2e8ee6f9")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-alabama", type=("build", "run"))
	depends_on("r-edger", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-tseries", type=("build", "run"))
	depends_on("r-vgam", type=("build", "run"))
	depends_on("r-ggplot2@2.2.1.9000:", type=("build", "run"))
	depends_on("r-nleqslv", type=("build", "run"))
	depends_on("r-phyloseq", type=("build", "run"))
	depends_on("r-tensor", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
