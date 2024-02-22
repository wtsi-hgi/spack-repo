# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStorm(RPackage):
	"""Write Storm Bolts in R using the Storm Multi-Language Protocol

	Storm is a distributed real-time computation system. Similar to how
 Hadoop provides a set of general primitives for doing batch processing, Storm
 provides a set of general primitives for doing real-time computation.

    Storm includes a "Multi-Language" (or "Multilang") Protocol to allow
 implementation of Bolts and Spouts in languages other than Java.  This R
 extension provides implementations of utility functions to allow an application
 developer to focus on application-specific functionality rather than Storm/R
 communications plumbing.
	"""
	
	cran = "Storm" 

	version("1.2", md5="72d1499e7149bc0867aae6261d35fc95")

	depends_on("r@2.1:", type=("build", "run"))
	depends_on("r-permute", type=("build", "run"))
	depends_on("r-rjson", type=("build", "run"))
