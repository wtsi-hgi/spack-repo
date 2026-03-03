# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSmaa(RPackage):
	"""Stochastic Multi-Criteria Acceptability Analysis

	Implementation of the Stochastic Multi-Criteria Acceptability Analysis (SMAA) family of Multiple Criteria Decision Analysis (MCDA) methods. Tervonen, T. and Figueira,  J. R. (2008) <doi:10.1002/mcda.407>.
	"""
	
	homepage = "https://github.com/gertvv/rsmaa"
	cran = "smaa" 

	version("0.3-2", md5="77d1586208b136bc7a89c7edc1700948")

