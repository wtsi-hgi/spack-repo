# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RProgress(RPackage):
	"""Terminal Progress Bars.

	Configurable Progress bars, they may include percentage, elapsed time,
	and/or the estimated completion time. They work in terminals, in 'Emacs'
	'ESS', 'RStudio', 'Windows' 'Rgui' and the 'macOS' 'R.app'.  The package
	also provides a 'C++' 'API', that works with or without 'Rcpp'."""

	cran = "progress"

	license("MIT")

	version("1.2.3", md5="db78636d2dd5ee346f5caf48bfa69f5e")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-hms", type=("build", "run"))
	depends_on("r-prettyunits", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
