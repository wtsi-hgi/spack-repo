# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMined(RPackage):
	"""Minimum Energy Designs

	This is a method (MinED) for mining probability distributions using deterministic sampling which is proposed by Joseph, Wang, Gu, Lv, and Tuo (2019) <DOI:10.1080/00401706.2018.1552203>. The MinED samples can be used for approximating the target distribution. They can be generated from a density function that is known only up to a proportionality constant and thus, it might find applications in Bayesian computation. Moreover, the MinED samples are generated with much fewer evaluations of the density function compared to random sampling-based methods such as MCMC and therefore, this method will be especially useful when the unnormalized posterior is expensive or time consuming to evaluate. This research is supported by a U.S. National Science Foundation grant DMS-1712642.
	"""
	
	cran = "mined" 

	version("1.0-3", md5="f8058608b2942bf5a3c26ec6b0f495fc")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
