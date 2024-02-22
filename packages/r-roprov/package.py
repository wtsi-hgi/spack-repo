# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRoprov(RPackage):
	"""Low-Level Support for Provenance Capture Between in-Memory R
Objects

	A suite of classes and methods which provide low-level support for modeling provenance between in-memory R objects. This is an infrastructure package and is not intended to be used directly by end-users.
	"""
	
	cran = "roprov" 

	version("0.1.2", md5="34ec7e5b45a1d86b0090dbbe90aeb1df")

	depends_on("r-fastdigest", type=("build", "run"))
	depends_on("r-codedepends@0.3.5:", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
