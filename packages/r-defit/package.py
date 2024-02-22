# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDefit(RPackage):
	"""Fitting Differential Equations to Time Series Data

	Use numerical optimization to fit ordinary differential equations (ODEs) to time series data to examine the dynamic relationships between variables or the characteristics of a dynamical system. It can now be used to estimate the parameters of ODEs up to second order, and can also apply to multilevel systems. See <https://github.com/yueqinhu/defit> for details.
	"""
	
	homepage = "https://github.com/yueqinhu/defit"
	cran = "deFit" 

	version("0.2.1", md5="af44c8f644add4592b419515aec39f4c")

	depends_on("r@3.50:", type=("build", "run"))
	depends_on("r-desolve", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
