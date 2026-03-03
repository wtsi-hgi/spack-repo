# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMix(RPackage):
	"""Estimation/Multiple Imputation for Mixed Categorical and
Continuous Data

	Estimation/multiple imputation programs for mixed categorical
    and continuous data.
	"""
	
	cran = "mix" 

	version("1.0-11", md5="a903261bb37381c9a82efa5754426920")

