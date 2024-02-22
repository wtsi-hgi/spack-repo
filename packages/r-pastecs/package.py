# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPastecs(RPackage):
	"""Package for Analysis of Space-Time Ecological Series

	Regularisation, decomposition and analysis of space-time series.
  The pastecs R package is a PNEC-Art4 and IFREMER (Benoit Beliaeff
  <Benoit.Beliaeff@ifremer.fr>) initiative to bring PASSTEC 2000 functionalities to R.
	"""
	
	homepage = "https://github.com/SciViews/pastecs"
	cran = "pastecs" 

	version("1.4.2", md5="9ae8c1a1da977897a3688f262bbc13c3")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
