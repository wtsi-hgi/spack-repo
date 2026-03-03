# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJgr(RPackage):
	"""Java GUI for R

	Java GUI for R - cross-platform, universal and unified Graphical User Interface for R. For full functionality on Windows and Mac OS X JGR requires a start application which depends on your OS.
	"""
	
	homepage = "https://rforge.net/JGR/"
	cran = "JGR" 

	version("1.9-2", md5="ec68e86b3543ec327a49f8e0a17b377d")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-rjava@1:", type=("build", "run"))
	depends_on("r-javagd@0.6:", type=("build", "run"))
	depends_on("openjdk@8:", type=("build", "link", "run"))
