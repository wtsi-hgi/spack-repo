# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTbfmultinomial(RPackage):
	"""TBF Methodology Extension for Multinomial Outcomes

	Extends the test-based Bayes factor (TBF) methodology to multinomial regression models and discrete time-to-event models with competing risks. The TBF methodology has been well developed and implemented for the generalised linear model [Held et al. (2015) <doi:10.1214/14-STS510>] and for the Cox model [Held et al. (2016) <doi:10.1002/sim.7089>].
	"""
	
	cran = "TBFmultinomial" 

	version("0.1.3", md5="cee5ca60ab34ffbaddbe2631719f6e0e")

	depends_on("r-vgam", type=("build", "run"))
	depends_on("r-nnet", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-plotrix", type=("build", "run"))
