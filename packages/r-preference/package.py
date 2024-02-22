# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPreference(RPackage):
	"""2-Stage Preference Trial Design and Analysis

	Design and analyze two-stage randomized trials with a continuous
    outcome measure. The package contains functions to compute the required 
    sample size needed to detect a given preference, treatment, and selection 
    effect; alternatively, the package contains functions that can report the 
    study power given a fixed sample size. Finally, analysis functions are 
    provided to test each effect using either summary data (i.e. means, 
    variances) or raw study data <doi:10.18637/jss.v094.c02>.
	"""
	
	homepage = "https://github.com/kaneplusplus/preference"
	cran = "preference" 

	version("1.1.6", md5="b0ee07f55b55e8402613c46a395756b8")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
