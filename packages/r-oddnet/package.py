# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROddnet(RPackage):
	"""Anomaly Detection in Temporal Networks

	Anomaly detection in dynamic, temporal networks. The package 
    'oddnet' uses a feature-based method to identify anomalies. First, it computes 
    many features for each network. Then it models the features using time series 
    methods. Using time series residuals it detects anomalies. This way, the 
    temporal dependencies are accounted for when identifying anomalies 
    (Kandanaarachchi, Hyndman 2022) <arXiv:2210.07407>.
	"""
	
	homepage = "https://sevvandi.github.io/oddnet/"
	cran = "oddnet" 

	version("0.1.1", md5="21b4d8f3786b55606211dcc6fea6a0d9")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-fable", type=("build", "run"))
	depends_on("r-fabletools", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-lookout", type=("build", "run"))
	depends_on("r-pcapp", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tsibble", type=("build", "run"))
