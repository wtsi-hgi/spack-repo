# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHellojavaworld(RPackage):
	"""Hello Java World

	A dummy package to demonstrate how to interface to a jar
        file that resides inside an R package.
	"""
	
	cran = "helloJavaWorld" 

	version("0.0-9", md5="311ed30c1e7cc44e21d66f0cf28d5db2")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-rjava@0.5.0:", type=("build", "run"))
	depends_on("openjdk@1.5:", type=("build", "link", "run"))
