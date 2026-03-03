# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRje(RPackage):
	"""Miscellaneous Useful Functions for Statistics

	A series of functions in some way considered useful to the author.  These 
    include methods for subsetting tables and generating indices for arrays, 
    conditioning and intervening in probability distributions, generating 
    combinations, fast transformations, and more...
	"""
	
	cran = "rje" 

	version("1.12.1", md5="56d7a0d2774bfadfb5028de8b6c5f040")

	depends_on("r@2:", type=("build", "run"))
