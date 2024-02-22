# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpgwr(RPackage):
	"""Geographically Weighted Regression

	Functions for computing geographically weighted
  regressions are provided, based on work by Chris
  Brunsdon, Martin Charlton and Stewart Fotheringham. 
	"""
	
	homepage = "https://github.com/rsbivand/spgwr/"
	cran = "spgwr" 

	version("0.6-36", md5="51cd285933c06b115802b301756bd29f")

	depends_on("r@2.14:", type=("build", "run"))
	depends_on("r-sp@0.8.3:", type=("build", "run"))
	depends_on("r-spdata@0.2.6.2:", type=("build", "run"))
