# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPurging(RPackage):
	"""Simple Method for Purging Mediation Effects among Independent
Variables

	Simple method of purging independent variables of mediating effects. First, regress the direct variable on the indirect variable. Then, used the stored residuals as the new purged (direct) variable in the updated specification. This purging process allows for use of a new direct variable uncorrelated with the indirect variable. Please cite the method and/or package using Waggoner, Philip D. (2018) <doi:10.1177/1532673X18759644>.
	"""
	
	cran = "purging" 

	version("1.0.0", md5="a19ded0299ec49312ec0799bd12ad99f")

	depends_on("r-mass", type=("build", "run"))
