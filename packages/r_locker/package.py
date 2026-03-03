# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLocker(RPackage):
	"""Locally Sparse Estimator of Generalized Varying Coefficient
Model for Asynchronous Longitudinal Data

	Locally sparse estimator of generalized varying coefficient model for asynchronous longitudinal data by kernel-weighted estimating equation.
	"""
	
	cran = "LocKer" 

	version("1.1", md5="6325e8d934275893b0ad285800216644")

	depends_on("r-fda", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-psych", type=("build", "run"))
