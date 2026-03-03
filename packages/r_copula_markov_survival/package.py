# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCopulaMarkovSurvival(RPackage):
	"""Copula Markov Model with Dependent Censoring

	Perform likelihood estimation and corresponding analysis under the copula-based Markov chain model for serially dependent event times with a dependent terminal event. Available are statistical methods in Huang, Wang and Emura (2020, JJSD accepted).
	"""
	
	cran = "Copula.Markov.survival" 

	version("1.0.0", md5="f1757c8af9755da2a3ec0d8be62e6686")

	depends_on("r-survival", type=("build", "run"))
