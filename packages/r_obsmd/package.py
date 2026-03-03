# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RObsmd(RPackage):
	"""Objective Bayesian Model Discrimination in Follow-Up Designs

	Implements the objective Bayesian methodology proposed in Consonni and Deldossi in order to choose the optimal experiment that better discriminate between competing models, see Deldossi and Nai Ruscone (2020) <doi:10.18637/jss.v094.i02>.
	"""
	
	cran = "OBsMD" 

	version("11.1", md5="d1822ac1f1acf0ac6f5e7ee41c409184")

