# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIndgenerrors(RPackage):
	"""Tests of Independence Between Innovations of Generalized Error
Models

	Computation of test statistics of independence between  (continuous) innovations of time series. They Can be used with stochastic volatility models and Hidden Markov Models (HMM). This improves the results in Duchesne, Ghoudi & Remillard (2012) <doi:10.1002/cjs.11141>.
	"""
	
	cran = "IndGenErrors" 

	version("0.1.4", md5="3cedbabdeff99437ad825661b3715041")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
