# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCdgd(RPackage):
	"""Causal Decomposition of Group Disparities

	The framework of causal decomposition of group disparities developed by
    Yu and Elwert (2023)
    <arXiv:2306.16591>.
    This package implements the decomposition estimators
    that are based on efficient influence functions. For the
    nuisance functions of the estimators, both parametric and
    nonparametric options are provided, as well as manual options in case
    the default models are not satisfying.
	"""
	
	homepage = "https://github.com/ang-yu/cdgd"
	cran = "cdgd" 

	version("0.3.4", md5="bd6a623d16262164fc2ff3a24883fd4c")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-caret@6:", type=("build", "run"))
