# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLog(RPackage):
	"""Record Events and Issues

	Logger to keep track of informational events and errors useful for debugging.
	"""
	
	cran = "log" 

	version("1.1.1", md5="65a908b59b8c320b9a862808c063bc6a")

	depends_on("r-r6", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
