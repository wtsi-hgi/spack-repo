# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpikes(RPackage):
	"""Detecting Election Fraud from Irregularities in Vote-Share
Distributions

	Applies re-sampled kernel density method to detect vote fraud. It estimates the proportion of coarse vote-shares in the observed data relative to the null hypothesis of no fraud.
	"""
	
	cran = "spikes" 

	version("1.1", md5="dbe7f4fbfa609ff3b6540ba84344a6e8")

	depends_on("r@3.2.2:", type=("build", "run"))
	depends_on("r-emdbook", type=("build", "run"))
