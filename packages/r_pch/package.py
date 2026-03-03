# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPch(RPackage):
	"""Piecewise Constant Hazard Models for Censored and Truncated Data

	Piecewise constant hazard models for survival data. 
    The package allows for right-censored, left-truncated, and interval-censored data.
	"""
	
	cran = "pch" 

	version("2.1", md5="f4f690ffa10977ed55012915a0ee9e32")

	depends_on("r-survival", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
