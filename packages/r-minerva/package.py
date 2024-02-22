# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMinerva(RPackage):
	"""Maximal Information-Based Nonparametric Exploration for Variable
Analysis

	Wrapper for 'minepy' implementation of Maximal
        Information-based Nonparametric Exploration statistics (MIC and
        MINE family). Detailed information of the ANSI C implementation of
	'minepy' can be found at <http://minepy.readthedocs.io/en/latest>.
	"""
	
	homepage = "https://www.r-project.org"
	cran = "minerva" 

	version("1.5.10", md5="378ffc5fd22accd1be8721ae3551c3cc")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
