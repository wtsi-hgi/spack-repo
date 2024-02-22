# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRkeajars(RPackage):
	"""R/KEA Interface Jars

	External jars required for package RKEA.
	"""
	
	cran = "RKEAjars" 

	version("5.0-4", md5="0d80ee16dfaf777aabf8d2f4417f51d0")

	depends_on("r-rjava@0.6.3:", type=("build", "run"))
	depends_on("openjdk@5:", type=("build", "link", "run"))
