# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPartdsa(RPackage):
	"""Partitioning Using Deletion, Substitution, and Addition Moves

	A novel tool for generating a piecewise
        constant estimation list of increasingly complex predictors
        based on an intensive and comprehensive search over the entire
        covariate space.
	"""
	
	cran = "partDSA" 

	version("0.9.14", md5="e563462fa979ca54680bb82b7cc7407c")

	depends_on("r@2.5:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
