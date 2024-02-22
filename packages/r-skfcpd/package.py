# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSkfcpd(RPackage):
	"""Fast Online Changepoint Detection for Temporally Correlated Data

	Sequential Kalman filter for scalable online changepoint detection by temporally correlated data. It enables fast single and multiple change points with missing values. See the reference: Hanmo Li, Yuedong Wang, Mengyang Gu (2023), <arXiv:2310.18611>.
	"""
	
	cran = "SKFCPD" 

	version("0.2.4", md5="db8278398114bd5bb1fbaef87a70737e")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rlang@1.0.6:", type=("build", "run"))
	depends_on("r-ggplot2@3.4:", type=("build", "run"))
	depends_on("r-ggpubr@0.5:", type=("build", "run"))
	depends_on("r-reshape2@1.4.4:", type=("build", "run"))
	depends_on("r-fastgasp@0.5.2:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
