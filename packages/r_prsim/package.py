# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPrsim(RPackage):
	"""Stochastic Simulation of Streamflow Time Series using Phase
Randomization

	Provides a simulation framework to simulate streamflow time series with similar main characteristics as observed data. These characteristics include the distribution of daily streamflow values and their temporal correlation as expressed by short- and long-range dependence. The approach is based on the randomization of the phases of the Fourier transform or the phases of the wavelet transform. The function prsim() is applicable to single site simulation and uses the Fourier transform. The function prsim.wave() extends the approach to multiple sites and is based on the complex wavelet transform. The function prsim.weather() extends the approach to multiple variables for weather generation. We further use the flexible four-parameter Kappa distribution, which allows for the extrapolation to yet unobserved low and high flows. Alternatively, the empirical or any other distribution can be used. 
  A detailed description of the simulation approach for single sites and an application example can be found in Brunner et al. (2019) <doi:10.5194/hess-23-3175-2019>.
  A detailed description and evaluation of the wavelet-based multi-site approach can be found in Brunner and Gilleland (2020) <doi:10.5194/hess-24-3967-2020>.
  A detailed description and evaluation of the multi-variable and multi-site weather generator can be found in Brunner et al. (2021) <doi:10.5194/esd-12-621-2021>.
	"""
	
	homepage = "https://git.math.uzh.ch/reinhard.furrer/PRSim-devel"
	cran = "PRSim" 

	version("1.4-4", md5="47f585ffe650b81517d6e1754e34cfaf")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-lmomco", type=("build", "run"))
	depends_on("r-mev", type=("build", "run"))
	depends_on("r-goftest", type=("build", "run"))
	depends_on("r-wavscalogram", type=("build", "run"))
	depends_on("r-splus2r", type=("build", "run"))
