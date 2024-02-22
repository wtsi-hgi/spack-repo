# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBtsr(RPackage):
	"""Bounded Time Series Regression

	Simulate, estimate and forecast a wide range of regression based dynamic models for bounded time series, covering the most commonly applied models in the literature. The main calculations are done in 'FORTRAN', which translates into very fast algorithms. The main references are 
   Bayer et al. (2017)  <doi:10.1016/j.jhydrol.2017.10.006>, 
   Pumi et al. (2019) <doi:10.1016/j.jspi.2018.10.001>, 
   Pumi et al. (2021) <doi:10.1111/sjos.12439> and 
	 Pumi et al. (2022) <arXiv:2211.02097>.
	"""
	
	cran = "BTSR" 

	version("0.1.5", md5="3d5ec1a6286be8ddf17404a5763974a8")

	depends_on("r@4:", type=("build", "run"))
