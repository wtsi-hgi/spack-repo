# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RW4mrutils(RPackage):
	"""Utils List for W4M - Workflow for Metabolomics

	Provides a set of utility function to prevent the spread of
    utilities script in W4M (Workflow4Metabolomics) scripts, and centralize
    them in a single package.
    Some are meant to be replaced by real packages in a near future, like
    the parse_args() function: it is here only to prepare the ground for
    more global changes in W4M scripts and tools.
	"""
	
	cran = "W4MRUtils" 

	version("1.0.0", md5="73ab5b508c72cc4811f037e58bc627d9")

	depends_on("r-rlang", type=("build", "run"))
