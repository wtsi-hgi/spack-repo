# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCosmos(RPackage):
	"""Complete Stochastic Modelling Solution

	Makes univariate, multivariate, or random fields simulations precise and simple. Just select the desired time series or random fields’ properties and it will do the rest. CoSMoS is based on the framework described in Papalexiou (2018, <doi:10.1016/j.advwatres.2018.02.013>), extended for random fields in Papalexiou and Serinaldi (2020, <doi:10.1029/2019WR026331>), and further advanced in Papalexiou et al. (2021, <doi:10.1029/2020WR029466>) to allow fine-scale space-time simulation of storms (or even cyclone-mimicking fields).
	"""
	
	homepage = "https://github.com/TycheLab/CoSMoS"
	cran = "CoSMoS" 

	version("2.1.0", md5="7197c1f1578603ea646ec8907762e9fc")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-nloptr", type=("build", "run"))
	depends_on("r-mba", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-mar", type=("build", "run"))
	depends_on("r-matrixcalc", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-directlabels", type=("build", "run"))
	depends_on("r-animation", type=("build", "run"))
	depends_on("r-ggquiver", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-plot3d", type=("build", "run"))
