# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RContingency(RPackage):
	"""Discrete Multivariate Probability Distributions

	Provides an object class for dealing with many multivariate
    probability distributions at once, useful for simulation.
	"""
	
	homepage = "https://github.com/rje42/contingency"
	cran = "contingency" 

	version("0.0.10", md5="78ea500c547f0e9b87adcd8d66501583")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rje", type=("build", "run"))
