# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSurrosurvroc(RPackage):
	"""Surrogate Survival ROC

	Nonparametric and semiparametric estimations of the time-dependent ROC curve for an incomplete failure time data with surrogate failure time endpoints.
	"""
	
	cran = "surrosurvROC" 

	version("0.1.0", md5="68c2cf92ccf853018e452fd139d6f2ae")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
