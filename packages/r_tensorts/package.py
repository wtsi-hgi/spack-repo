# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTensorts(RPackage):
	"""Factor and Autoregressive Models for Tensor Time Series

	Factor and autoregressive models for matrix and tensor valued time series. We provide functions for estimation, simulation and prediction. The models are discussed in 
    Li et al (2021) <arXiv:2110.00928>, Chen et al (2020) <DOI:10.1080/01621459.2021.1912757>, 
    Chen et al (2020) <DOI:10.1016/j.jeconom.2020.07.015>, and Xiao et al (2020) <arXiv:2006.02611>.
	"""
	
	homepage = "https://github.com/zebang/tensorTS"
	cran = "tensorTS" 

	version("1.0.1", md5="9564d9af614803552aa2ea903ee92e45")

	depends_on("r-tensor", type=("build", "run"))
	depends_on("r-rtensor", type=("build", "run"))
	depends_on("r-expm", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
