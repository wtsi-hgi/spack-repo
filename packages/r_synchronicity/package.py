# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSynchronicity(RPackage):
	"""Boost Mutex Functionality in R

	Boost mutex functionality in R.
	"""
	
	homepage = "http://www.bigmemory.org"
	cran = "synchronicity" 

	version("1.3.10", md5="09dc87b9cfd169b9e57fbe05aa9762a2")

	depends_on("r-bigmemory-sri", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-uuid", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
