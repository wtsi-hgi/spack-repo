# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHttpgd(RPackage):
	"""A 'HTTP' Server Graphics Device

	A graphics device for R that is accessible via network protocols.
    This package was created to make it easier to embed live R graphics in 
    integrated development environments and other applications.
    The included 'HTML/JavaScript' client (plot viewer) aims to provide a better overall user experience when dealing with R graphics.
    The device asynchronously serves graphics via 'HTTP' and 'WebSockets'.
	"""
	
	homepage = "https://github.com/nx10/httpgd"
	cran = "httpgd" 

	version("2.0.1", md5="2c18e37c6f9c36f743ce8b467ab370cd")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-unigd", type=("build", "run"))
	depends_on("r-cpp11@0.2.4:", type=("build", "run"))
	depends_on("r-asioheaders@1.22.1:", type=("build", "run"))
