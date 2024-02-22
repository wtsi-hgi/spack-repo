# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJoiner(RPackage):
	"""Joint Modelling of Repeated Measurements and Time-to-Event Data

	Analysis of repeated measurements and time-to-event data via random
    effects joint models. Fits the joint models proposed by Henderson and colleagues
    <doi:10.1093/biostatistics/1.4.465> (single event time) and by Williamson and
    colleagues (2008) <doi:10.1002/sim.3451> (competing risks events time) to a
    single continuous repeated measure. The time-to-event data is modelled using a 
    (cause-specific) Cox proportional hazards regression model with time-varying 
    covariates. The longitudinal outcome is modelled using a linear mixed effects
    model. The association is captured by a latent Gaussian process. The model is 
    estimated using am Expectation Maximization algorithm. Some plotting functions 
    and the variogram are also included. This project is funded by the Medical 
    Research Council (Grant numbers G0400615 and MR/M013227/1).
	"""
	
	homepage = "https://github.com/graemeleehickey/joineR/"
	cran = "joineR" 

	version("1.2.8", md5="60f5c4cf642372b3905ffd58097eb1bd")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-statmod", type=("build", "run"))
