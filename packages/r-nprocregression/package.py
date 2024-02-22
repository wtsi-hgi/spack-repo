# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNprocregression(RPackage):
	"""Kernel-Based Nonparametric ROC Regression Modelling

	Implements several nonparametric regression approaches for the inclusion of covariate information on the receiver operating characteristic (ROC) framework.
	"""
	
	cran = "npROCRegression" 

	version("1.0-7", md5="d034df97b8671a4a97de1d5ddef662e7")

	depends_on("r-lattice", type=("build", "run"))
