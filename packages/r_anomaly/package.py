# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAnomaly(RPackage):
	"""Detecting Anomalies in Data

	Implements Collective And Point Anomaly (CAPA) Fisch, Eckley, and Fearnhead (2022) <doi:10.1002/sam.11586>, Multi-Variate Collective And Point Anomaly (MVCAPA) Fisch, Eckley, and Fearnhead (2021) <doi:10.1080/10618600.2021.1987257>, Proportion Adaptive Segment Selection (PASS) Jeng, Cai, and Li (2012) <doi:10.1093/biomet/ass059>, and Bayesian Abnormal Region Detector (BARD) Bardwell and Fearnhead (2015) <arXiv:1412.5565>. These methods are for the detection of anomalies in time series data. 
	"""
	
	cran = "anomaly" 

	version("4.3.2", md5="3af3c3b4597ef17a849d6f8ddaa4ba63")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-xts", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
