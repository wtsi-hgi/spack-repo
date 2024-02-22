# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCtsemomx(RPackage):
	"""Continuous Time SEM - 'OpenMx' Based Functions

	Original 'ctsem' (continuous time structural equation modelling)
    functionality, based on the 'OpenMx' software, as described in 
    Driver, Oud, Voelkle (2017) <doi:10.18637/jss.v077.i05>, with updated details in vignette. 
    Combines stochastic differential equations representing latent processes with 
    structural equation measurement models. These functions were split off from
    the main package of 'ctsem', as the main package uses the 'rstan' package as a backend now --
    offering estimation options from max likelihood to Bayesian.
    There are nevertheless use cases for the wide format SEM style approach as offered here, 
    particularly when there are no individual differences in observation timing and the
    number of individuals is large. For the main 'ctsem' package, see <https://cran.r-project.org/package=ctsem>.
	"""
	
	homepage = "https://github.com/cdriveraus/ctsemOMX"
	cran = "ctsemOMX" 

	version("1.0.6", md5="499d8ca7ea5fb510a68349495c8afb7f")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ctsem@3.3.2:", type=("build", "run"))
	depends_on("r-openmx@2.9:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
