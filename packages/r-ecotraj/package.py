# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REcotraj(RPackage):
	"""Ecological Trajectory Analysis

	Assists ecologists in the analysis of temporal changes of 
    ecosystems, defined as trajectories on a chosen multivariate space, by providing a set of 
    trajectory metrics and visual representations [De Caceres et al. (2019) <doi:10.1002/ecm.1350>; 
    and Sturbois et al. (2021) <doi:10.1016/j.ecolmodel.2020.109400>]. Includes functions
    to estimate metrics for individual trajectories (length, directionality, angles, ...) as well as
    metrics to relate pairs of trajectories (dissimilarity and convergence). Functions are also
    provided to estimate the ecological quality of ecosystem with respect to reference conditions 
    [Sturbois et al. (2023) ].
	"""
	
	homepage = "https://emf-creaf.github.io/ecotraj/"
	cran = "ecotraj" 

	version("0.1.1", md5="f8cb8cf522e85ca6549eed890c16cfa8")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-kendall", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
