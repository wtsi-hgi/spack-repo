# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRmWeights(RPackage):
	"""Weighted Rasch Modeling and Extensions using Conditional Maximum
Likelihood

	Rasch model and extensions for survey data, using Conditional Maximum likelihood (CML). Carlo Cafiero, Sara Viviani, Mark Nord (2018) <doi:10.1016/j.measurement.2017.10.065>.
	"""
	
	cran = "RM.weights" 

	version("2.0", md5="a2df0254d7e194673f86da9439c89f2a")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-psychotools", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
