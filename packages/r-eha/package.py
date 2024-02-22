# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REha(RPackage):
	"""Event History Analysis

	Parametric proportional hazards fitting with left truncation and
        right censoring for common families of distributions, piecewise constant 
        hazards, and discrete models. Parametric accelerated failure time models
        for left truncated and right censored data. Proportional hazards
        models for tabular and register data. Sampling of risk sets in Cox 
        regression, selections in the Lexis diagram, bootstrapping. 
        Broström (2022) <doi:10.1201/9780429503764>.
	"""
	
	homepage = "https://ehar.se/r/eha/"
	cran = "eha" 

	version("2.11.2", md5="8522414c74f0505eb4b6b9c0ec4fba9f")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-survival@3:", type=("build", "run"))
