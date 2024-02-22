# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRainfarmr(RPackage):
	"""Stochastic Precipitation Downscaling with the RainFARM Method

	An implementation of the RainFARM (Rainfall Filtered Autoregressive Model) stochastic precipitation downscaling method (Rebora et al. (2006) <doi:10.1175/JHM517.1>). Adapted for climate downscaling according to D'Onofrio et al. (2018) <doi:10.1175/JHM-D-13-096.1> and for complex topography as in Terzago et al. (2018) <doi:10.5194/nhess-18-2825-2018>. The RainFARM method is based on the extrapolation to small scales of the Fourier spectrum of a large-scale precipitation field, using a fixed logarithmic slope and random phases at small scales, followed by a nonlinear transformation of the resulting linearly correlated stochastic field. RainFARM allows to generate ensembles of spatially downscaled precipitation fields which conserve precipitation at large scales and whose statistical properties are consistent with the small-scale statistics of observed precipitation, based only on knowledge of the large-scale precipitation field.
	"""
	
	homepage = "https://github.com/jhardenberg/rainfarmr"
	cran = "rainfarmr" 

	version("0.1", md5="f55842f29485c62c7c5a03fe18ccbc2f")

	depends_on("r@3.1:", type=("build", "run"))
