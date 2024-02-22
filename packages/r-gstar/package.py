# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGstar(RPackage):
	"""Generalized Space-Time Autoregressive Model

	Multivariate time series analysis based on Generalized Space-Time Autoregressive Model by Ruchjana et al.(2012) <doi:10.1063/1.4724118>.
	"""
	
	cran = "gstar" 

	version("0.1.0", md5="e116a3d682985caf112f8e1568e9ace9")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-xts", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
