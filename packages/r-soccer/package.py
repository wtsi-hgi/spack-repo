# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSoccer(RPackage):
	"""Evaluating Sport Tournament Predictions

	Functions for evaluating tournament predictions, simulating results from individual soccer matches and tournaments. See <http://sandsynligvis.dk/2018/08/03/world-cup-prediction-winners/> for more information.
	"""
	
	homepage = "https://github.com/ekstroem/socceR"
	cran = "socceR" 

	version("0.1.1", md5="02b89826b6d0f1d99937966ebd03b3cf")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
