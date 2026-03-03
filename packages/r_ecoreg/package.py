# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REcoreg(RPackage):
	"""Ecological Regression using Aggregate and Individual Data

	Estimating individual-level covariate-outcome associations 
 using aggregate data ("ecological inference") or a combination of 
 aggregate and individual-level data ("hierarchical related regression").
	"""
	
	cran = "ecoreg" 

	version("0.2.4", md5="f39cf562d1e6e85a3af109a96695f7fc")

