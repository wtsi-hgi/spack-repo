# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFrackrigingr(RPackage):
	"""Spatial Multivariate Data Modeling

	Aim is to provide fractional Brownian vector field generation algorithm, Hurst parameter estimation method and fractional kriging model for multivariate data modeling.
	"""
	
	homepage = "https://github.com/NidaGreen/FracKriging"
	cran = "FracKrigingR" 

	version("1.0.0", md5="0e450bcf3776ed3a2695a7232ea7fbea")

	depends_on("r-psych", type=("build", "run"))
	depends_on("r-clustergeneration", type=("build", "run"))
