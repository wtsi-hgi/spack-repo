# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMixphm(RPackage):
	"""Mixtures of Proportional Hazard Models

	Fits multiple variable mixtures of various parametric proportional hazard models using the EM-Algorithm. Proportionality restrictions can be imposed on the latent groups and/or on the variables. Several survival distributions can be specified. Missing values and censored values are allowed. Independence is assumed over the single variables.
	"""
	
	cran = "mixPHM" 

	version("0.7-2", md5="8f15a0bbb92ff65fe6a14d4350f691df")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
