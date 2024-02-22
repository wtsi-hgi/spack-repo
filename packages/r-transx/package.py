# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTransx(RPackage):
	"""Transform Univariate Time Series

	Univariate time series operations that follow an opinionated design. 
    The main principle of 'transx' is to keep the number of observations the same. 
    Operations that reduce this number have to fill the observations gap.
	"""
	
	homepage = "https://github.com/kvasilopoulos/transx"
	cran = "transx" 

	version("0.0.1", md5="eac54cec7c28726d5380971e2df5843f")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
