# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSubgroup(RPackage):
	"""Methods for exploring treatment effect heterogeneity in subgroup
analysis of clinical trials

	Produces various measures of expected treatment effect heterogeneity under an assumption of homogeneity across subgroups. Graphical presentations are created to compare these expected differences with the observed differences.
	"""
	
	cran = "subgroup" 

	version("1.1", md5="ac8cc15fabc25c132ed93fba05ff2eda")

	depends_on("r@3.1:", type=("build", "run"))
