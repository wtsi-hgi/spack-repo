# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPasso(RPackage):
	"""Assessing the Partial Association Between Ordinal Variables

	An implementation of the unified framework for assessing partial association 
            between ordinal variables after adjusting for a set of covariates (Dungang Liu, Shaobo 
            Li, Yan Yu and Irini Moustaki (2020), accepted by the Journal of the American 
            Statistical Association). This package provides a set of tools to quantify, visualize, 
            and test partial associations between multiple ordinal variables. It can produce a number
            of $phi$ measures, partial regression plots, 3-D plots, and $p$-values for testing 
            $H_0: phi=0$ or $H_0: phi <= delta$.
	"""
	
	homepage = "GitHub:"
	cran = "PAsso" 

	version("0.1.10", md5="b50c016f6b40e529fc89cdf93720011c")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2@2.2.1:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-vgam", type=("build", "run"))
	depends_on("r-copbasic", type=("build", "run"))
	depends_on("r-pcapp@1.9.73:", type=("build", "run"))
	depends_on("r-foreach@1.4.8:", type=("build", "run"))
	depends_on("r-mass@7.3.51:", type=("build", "run"))
	depends_on("r-ggally", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-progress@1.2:", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-copula", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
