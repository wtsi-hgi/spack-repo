# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGarchsk(RPackage):
	"""Estimating a GARCHSK Model and GJRSK Model

	Functions for estimating a GARCHSK model and GJRSK model based on a publication by Leon et,al (2005)<doi:10.1016/j.qref.2004.12.020> and Nakagawa and Uchiyama (2020)<doi:10.3390/math8111990>. These are a GARCH-type model allowing for time-varying volatility, skewness and kurtosis.
	"""
	
	cran = "GARCHSK" 

	version("0.1.0", md5="cbb8eb376e8aeb5f44f920bc034f3d4a")

	depends_on("r-rsolnp", type=("build", "run"))
