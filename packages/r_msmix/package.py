# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMsmix(RPackage):
	"""Finite Mixtures of Mallows Models with Spearman Distance for
Full and Partial Rankings

	Fit and analysis of finite Mixtures of Mallows models with Spearman Distance for full and partial rankings with arbitrary missing positions. Inference is conducted within the maximum likelihood framework via Expectation-Maximization algorithms. Estimation uncertainty is tackled via diverse versions of bootstrapping as well as via Hessian-based standard errors calculations. The most relevant reference of the methods is Crispino, Mollica, Astuti and Tardella (2023) <doi:10.1007/s11222-023-10266-8>.
	"""
	
	cran = "MSmix" 

	version("1.0.0", md5="5ea0743815fc04166c3561002d153112")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-bayesmallows@2.0.1:", type=("build", "run"))
	depends_on("r-bmixture@1.7:", type=("build", "run"))
	depends_on("r-data-table@1.15:", type=("build", "run"))
	depends_on("r-dplyr@1.1.4:", type=("build", "run"))
	depends_on("r-factoextra@1.0.7:", type=("build", "run"))
	depends_on("r-fields@15.2:", type=("build", "run"))
	depends_on("r-foreach@1.5.2:", type=("build", "run"))
	depends_on("r-ggbump@0.1:", type=("build", "run"))
	depends_on("r-ggplot2@3.4.4:", type=("build", "run"))
	depends_on("r-gridextra@2.3:", type=("build", "run"))
	depends_on("r-rankcluster@0.98:", type=("build", "run"))
	depends_on("r-rcolorbrewer@1.1.3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-reshape@0.8.9:", type=("build", "run"))
	depends_on("r-rlang@1.1.3:", type=("build", "run"))
	depends_on("r-spsutil@0.2.2:", type=("build", "run"))
	depends_on("r-stringr@1.5.1:", type=("build", "run"))
