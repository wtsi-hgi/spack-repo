# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPlu(RPackage):
	"""Dynamically Pluralize Phrases

	Converts English phrases to singular or plural form based on
    the length of an associated vector.  Contains helper functions to
    create natural language lists from vectors and to include the length
    of a vector in natural language.
	"""
	
	homepage = "https://pkg.rossellhayes.com/plu/"
	cran = "plu" 

	version("0.3.0", md5="3bcfd18ee3f6828462909ea4401d8c22")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
