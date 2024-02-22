# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMcmcplots(RPackage):
	"""Create Plots from MCMC Output

	Functions for convenient plotting and viewing of MCMC output.
	"""
	
	cran = "mcmcplots" 

	version("0.4.3", md5="01d3c376f66b5b200191e6c0c138b524")

	depends_on("r-coda@0.17.1:", type=("build", "run"))
	depends_on("r-sfsmisc", type=("build", "run"))
	depends_on("r-colorspace", type=("build", "run"))
	depends_on("r-denstrip", type=("build", "run"))
