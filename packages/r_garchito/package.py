# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGarchito(RPackage):
	"""Class of GARCH-Ito Models

	Provides functions to estimate model parameters and forecast future volatilities using the Unified GARCH-Ito [Kim and Wang (2016) <doi:10.1016/j.jeconom.2016.05.003>] and Realized GARCH-Ito [Song et. al. (2020) <doi:10.1016/j.jeconom.2020.07.007>] models. Optimization is done using augmented Lagrange multiplier method.  
	"""
	
	cran = "GARCHIto" 

	version("0.1.0", md5="c67e4b2bb0ae63952ad3b88a907fdf3e")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rsolnp", type=("build", "run"))
