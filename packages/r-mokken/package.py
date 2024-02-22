# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMokken(RPackage):
	"""Conducts Mokken Scale Analysis

	Contains functions for performing Mokken
   scale analysis on test and questionnaire data.
   It includes an automated item selection algorithm, and various checks of model assumptions.
	"""
	
	homepage = "https://sites.google.com/a/tilburguniversity.edu/avdrark/mokken"
	cran = "mokken" 

	version("3.1.0", md5="44678e87ccd6e84f704ec2651ef60368")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-polca", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
