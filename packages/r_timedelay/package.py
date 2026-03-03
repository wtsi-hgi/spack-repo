# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTimedelay(RPackage):
	"""Time Delay Estimation for Stochastic Time Series of
Gravitationally Lensed Quasars

	We provide a toolbox to estimate the time delay between the brightness time series of gravitationally lensed quasar images via Bayesian and profile likelihood approaches. The model is based on a state-space representation for  irregularly observed time series data generated from a latent continuous-time Ornstein-Uhlenbeck process. Our Bayesian method adopts scientifically motivated hyper-prior distributions and a Metropolis-Hastings within Gibbs sampler, producing posterior samples of the model parameters that include the time delay. A profile likelihood of the time delay is a simple approximation to the marginal posterior distribution of the time delay. Both Bayesian and profile likelihood approaches complement each other, producing almost identical results; the Bayesian way is more principled but the profile likelihood is easier to implement. A new functionality is added in version 1.0.9 for estimating the time delay between doubly-lensed light curves observed in two bands. See also Tak et al. (2017) <doi:10.1214/17-AOAS1027>, Tak et al. (2018) <doi:10.1080/10618600.2017.1415911>, Hu and Tak (2020) <arXiv:2005.08049>.
	"""
	
	cran = "timedelay" 

	version("1.0.11", md5="7eb459e072d197e9f64ce0466c4193fd")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mass@7.3.51.3:", type=("build", "run"))
	depends_on("r-mvtnorm@1.0.11:", type=("build", "run"))
