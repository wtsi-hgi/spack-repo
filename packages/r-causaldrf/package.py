# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCausaldrf(RPackage):
	"""Estimating Causal Dose Response Functions

	Functions and data to estimate causal dose response functions given continuous, ordinal, or binary treatments.  A description of the methods is given in Galagate (2016) <https://drum.lib.umd.edu/handle/1903/18170>.
	"""
	
	cran = "causaldrf" 

	version("0.4.2", md5="4c7a412efa1076d0c67b839099b2efef")

	depends_on("r@3.1.2:", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-survey", type=("build", "run"))
