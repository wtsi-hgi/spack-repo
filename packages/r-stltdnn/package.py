# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStltdnn(RPackage):
	"""STL Decomposition and TDNN Hybrid Time Series Forecasting

	Implementation of hybrid STL decomposition based time delay neural network model for univariate time series forecasting. For method details see Jha G K, Sinha, K (2014). <doi:10.1007/s00521-012-1264-z>, Xiong T, Li C, Bao Y (2018). <doi:10.1016/j.neucom.2017.11.053>. 
	"""
	
	cran = "stlTDNN" 

	version("0.1.0", md5="47232cc66f59dc7e7468d02481d108e8")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-forecast", type=("build", "run"))
	depends_on("r-nnfor", type=("build", "run"))
