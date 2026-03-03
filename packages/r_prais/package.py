# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPrais(RPackage):
	"""Prais-Winsten Estimator for AR(1) Serial Correlation

	The Prais-Winsten estimator (Prais & Winsten, 1954) takes into account AR(1) serial correlation of the errors in a linear regression model. The procedure recursively estimates the coefficients and the error autocorrelation of the specified model until sufficient convergence of the AR(1) coefficient is attained.
	"""
	
	homepage = "https://github.com/franzmohr/prais"
	cran = "prais" 

	version("1.1.2", md5="7a24f2a38f982dc9b354f120594dfe41")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-sandwich", type=("build", "run"))
	depends_on("r-pcse", type=("build", "run"))
	depends_on("r-lmtest", type=("build", "run"))
