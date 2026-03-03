# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAcp(RPackage):
	"""Autoregressive Conditional Poisson

	Analysis of count data exhibiting autoregressive properties, using the Autoregressive Conditional Poisson model (ACP(p,q)) proposed by Heinen (2003).
	"""
	
	cran = "acp" 

	version("2.1", md5="d27ec8c2465e7cada6926f6585c91c12")

	depends_on("r-tseries", type=("build", "run"))
	depends_on("r-quantmod", type=("build", "run"))
