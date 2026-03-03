# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMagicaxis(RPackage):
	"""Pretty Scientific Plotting with Minor-Tick and Log Minor-Tick
Support

	Functions to make useful (and pretty) plots for scientific plotting. Additional plotting features are added for base plotting, with particular emphasis on making attractive log axis plots.
	"""
	
	cran = "magicaxis" 

	version("2.4.5", md5="d243dc8ef8858161e738194ce2728ca7")

	depends_on("r-celestial@1.4.1:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-plotrix", type=("build", "run"))
	depends_on("r-sm", type=("build", "run"))
	depends_on("r-mapproj", type=("build", "run"))
	depends_on("r-rann", type=("build", "run"))
