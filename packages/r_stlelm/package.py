# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStlelm(RPackage):
	"""Hybrid Forecasting Model Based on STL Decomposition and ELM

	Univariate time series forecasting with STL decomposition based Extreme Learning Machine hybrid  model. For method details see Xiong T, Li C, Bao Y (2018). <doi:10.1016/j.neucom.2017.11.053>. 
	"""
	
	cran = "stlELM" 

	version("0.1.1", md5="94109f89d2747b14146404284679f193")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-forecast", type=("build", "run"))
	depends_on("r-nnfor", type=("build", "run"))
