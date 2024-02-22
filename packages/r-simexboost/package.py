# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSimexboost(RPackage):
	"""Boosting Method for High-Dimensional Error-Prone Data

	Implementation of the boosting procedure with the simulation and extrapolation approach to address variable selection and estimation for high-dimensional data subject to measurement error in predictors. It can be used to address generalized linear models (GLM) in Chen (2023) <doi: 10.1007/s11222-023-10209-3> and the accelerated failure time (AFT) model in Chen and Qiu (2023) <doi: 10.1111/biom.13898>. Some relevant references include Chen and Yi (2021) <doi:10.1111/biom.13331> and Hastie, Tibshirani, and Friedman (2008, ISBN:978-0387848570).
	"""
	
	cran = "SIMEXBoost" 

	version("0.2.0", md5="0557c0f2de17cef5e347e0dfc958c341")

	depends_on("r-mass", type=("build", "run"))
