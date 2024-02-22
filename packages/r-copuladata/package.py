# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCopuladata(RPackage):
	"""Data Sets for Copula Modeling

	Data sets used for copula modeling in addition to those in
 the package 'copula'. These include a random subsample from the US National
 Education Longitudinal Study (NELS) of 1988 and nursing home data from
 Wisconsin.
	"""
	
	homepage = "http://copula.r-forge.r-project.org/"
	cran = "copulaData" 

	version("0.0-1", md5="f5b1849e1490da58c511532668ed2586")

	depends_on("r@3.1:", type=("build", "run"))
