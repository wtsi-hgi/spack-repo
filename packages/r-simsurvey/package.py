# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSimsurvey(RPackage):
	"""Test Surveys by Simulating Spatially-Correlated Populations

	Simulate age-structured populations that vary in space and time and 
    explore the efficacy of a range of built-in or user-defined sampling 
    protocols to reproduce the population parameters of the known population. 
    (See Regular et al. (2020) <doi:10.1371/journal.pone.0232822> for more
    details).
	"""
	
	homepage = "https://paulregular.github.io/SimSurvey/"
	cran = "SimSurvey" 

	version("0.1.6", md5="7979aec7e1a67915b8ce0164ee6e899e")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-stars", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
