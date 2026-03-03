# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDiffusion(RPackage):
	"""Forecast the Diffusion of New Products

	Various diffusion models to forecast new product growth. Currently
    the package contains Bass, Gompertz and Gamma/Shifted Gompertz curves. See
    Meade and Islam (2006) <doi:10.1016/j.ijforecast.2006.01.005>.
	"""
	
	homepage = "https://github.com/mamut86/diffusion"
	cran = "diffusion" 

	version("0.2.7", md5="42ee50b4e7f5014f7d128a7c98925509")

	depends_on("r-dfoptim", type=("build", "run"))
	depends_on("r-nloptr", type=("build", "run"))
	depends_on("r-systemfit", type=("build", "run"))
