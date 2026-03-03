# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTkrplot(RPackage):
	"""TK Rplot

	Simple mechanism for placing R graphics in a Tk widget.
	"""
	
	cran = "tkrplot" 

	version("0.0-27", md5="727386b682aa072923457b9ca5ab993f")

	depends_on("r@2.13:", type=("build", "run"))
	depends_on("libx11", type=("build", "link", "run"))
	depends_on("libxext", type=("build", "link", "run"))
	depends_on("libxscrnsaver", type=("build", "link", "run"))
