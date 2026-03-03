# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTsrobprep(RPackage):
	"""Robust Preprocessing of Time Series Data

	Methods for handling the missing values outliers are introduced in
    this package. The recognized missing values and outliers are replaced 
    using a model-based approach. The model may consist of both autoregressive
    components and external regressors. The methods work robust and efficient,
    and they are fully tunable. The primary motivation for writing the package
    was preprocessing of the energy systems data, e.g. power plant production
    time series, but the package could be used with any time series data. For 
    details, see Narajewski et al. (2021) <doi:10.1016/j.softx.2021.100809>.
	"""
	
	cran = "tsrobprep" 

	version("0.3.2", md5="4714cd3fc85a319aa761d02d616fa82c")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-mclust", type=("build", "run"))
	depends_on("r-quantreg", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-texttinyr", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
