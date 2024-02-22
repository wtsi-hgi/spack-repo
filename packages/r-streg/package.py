# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStreg(RPackage):
	"""Student's t Regression Models

	It contains functions to estimate multivariate Student's t dynamic and static regression models for given degrees of freedom and lag length. Users can also specify the trends and dummies of any kind in matrix form.
    Poudyal, N., and Spanos, A. (2022) <doi:10.3390/econometrics10020017>.
    Spanos, A. (1994) <http://www.jstor.org/stable/3532870>.
	"""
	
	cran = "StReg" 

	version("1.1", md5="321e4b3e4b8c3a07dd9f8124c9139fb2")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-adgoftest", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-mcmcpack", type=("build", "run"))
	depends_on("r-matlab", type=("build", "run"))
	depends_on("r-tseries", type=("build", "run"))
