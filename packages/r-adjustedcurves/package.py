# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAdjustedcurves(RPackage):
	"""Confounder-Adjusted Survival Curves and Cumulative Incidence
Functions

	Estimate and plot confounder-adjusted survival curves using
    either 'Direct Adjustment', 'Direct Adjustment with Pseudo-Values',
    various forms of 'Inverse Probability of Treatment Weighting', two
    forms of 'Augmented Inverse Probability of Treatment Weighting',
    'Empirical Likelihood Estimation' or 'Targeted Maximum Likelihood Estimation'.
	Also includes a significance test for the difference
    between two adjusted survival curves and the calculation of adjusted
    restricted mean survival times.  Additionally enables the user to
    estimate and plot cause-specific confounder-adjusted cumulative
    incidence functions in the competing risks setting using the same
    methods (with some exceptions).
	For details, see Denz et. al (2023) <doi:10.1002/sim.9681>.
	"""
	
	homepage = "https://github.com/RobinDenz1/adjustedCurves"
	cran = "adjustedCurves" 

	version("0.11.0", md5="b2b6ec4cd09356136d3f36a0ca7a0b2d")

	depends_on("r-r-utils", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-dorng", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
