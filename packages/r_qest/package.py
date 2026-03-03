# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQest(RPackage):
	"""Quantile-Based Estimator

	Quantile-based estimators (Q-estimators) can be used to fit any parametric distribution, using its quantile function. Q-estimators are usually more robust than standard maximum likelihood estimators. The method is described in: Sottile G. and Frumento P. (2022). Robust estimation and regression with parametric quantile functions. <doi:10.1016/j.csda.2022.107471>.
	"""
	
	homepage = "https://www.sciencedirect.com/science/article/abs/pii/S0167947322000512"
	cran = "Qest" 

	version("1.0.1", md5="7fb8d5bf67f8b9ad7de401f84f02ae47")

	depends_on("r-pch", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
