# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCoarsedatatools(RPackage):
	"""Analysis of Coarsely Observed Data

	Functions to analyze coarse data.
    Specifically, it contains functions to (1) fit parametric accelerated
    failure time models to interval-censored survival time data, and (2)
    estimate the case-fatality ratio in scenarios with under-reporting.
    This package's development was motivated by applications to infectious
    disease: in particular, problems with estimating the incubation period and
    the case fatality ratio of a given disease.  Sample data files are included
    in the package. See Reich et al. (2009) <doi:10.1002/sim.3659>, 
    Reich et al. (2012) <doi:10.1111/j.1541-0420.2011.01709.x>, and 
    Lessler et al. (2009) <doi:10.1016/S1473-3099(09)70069-6>.
	"""
	
	homepage = "https://cran.r-project.org/package=coarseDataTools"
	cran = "coarseDataTools" 

	version("0.6-6", md5="436114e13da8e2f3f59c47fcc4392f8a")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mcmcpack", type=("build", "run"))
