# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFmadist(RPackage):
	"""Frequentist Model Averaging Distribution

	Creation of an input model (fitted distribution) via the frequentist model averaging (FMA) approach and generate random-variates from the distribution specified by "myfit" which is the fitted input model via the FMA approach. See W. X. Jiang and B. L. Nelson (2018), "Better Input Modeling via Model Averaging," Proceedings of the 2018 Winter Simulation Conference, IEEE Press, 1575-1586.
	"""
	
	cran = "FMAdist" 

	version("0.1.2", md5="1aac0bd463c5e9c2b37b9cdaf85bb640")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-fitdistrplus", type=("build", "run"))
	depends_on("r-actuar", type=("build", "run"))
	depends_on("r-envstats", type=("build", "run"))
	depends_on("r-extradistr", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-quadprog", type=("build", "run"))
