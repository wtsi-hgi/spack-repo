# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLsasim(RPackage):
	"""Functions to Facilitate the Simulation of Large Scale Assessment
Data

	Provides functions to simulate data from large-scale educational
  assessments, including background questionnaire data and cognitive item
  responses that adhere to a multiple-matrix sampled design. The theoretical
  foundation can be found on
  Matta, T.H., Rutkowski, L., Rutkowski, D. et al. (2018)
  <doi:10.1186/s40536-018-0068-8>.
	"""
	
	cran = "lsasim" 

	version("2.1.4", md5="5e15e10e5bed5226a8f44da24eed5dc2")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-polycor", type=("build", "run"))
