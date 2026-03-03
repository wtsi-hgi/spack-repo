# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBrxx(RPackage):
	"""Bayesian Test Reliability Estimation

	When samples contain missing data, are small, or are suspected of bias,
    estimation of scale reliability may not be trustworthy.  A recommended solution
    for this common problem has been Bayesian model estimation.  Bayesian methods
    rely on user specified information from historical data or researcher intuition 
    to more accurately estimate the parameters.  This package provides a user friendly
    interface for estimating test reliability.  Here, reliability is modeled as a beta
    distributed random variable with shape parameters alpha=true score variance and
    beta=error variance (Tanzer & Harlow, 2020) <doi:10.1080/00273171.2020.1854082>.
	"""
	
	cran = "brxx" 

	version("0.1.2", md5="bb80866a18b0c5f5936fd195a1951376")

	depends_on("r-mcmcpack", type=("build", "run"))
	depends_on("r-gparotation", type=("build", "run"))
	depends_on("r-teachingdemos", type=("build", "run"))
	depends_on("r-blavaan", type=("build", "run"))
	depends_on("r-blme", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rstan", type=("build", "run"))
