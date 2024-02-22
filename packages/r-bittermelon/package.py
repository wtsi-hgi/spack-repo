# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBittermelon(RPackage):
	"""Monochrome Bitmap Font Tools

	Provides functions for creating and modifying bitmaps with special emphasis on bitmap fonts and their glyphs.  Provides native read/write support for the 'hex' and 'yaff' bitmap font formats and if 'Python' is installed can also read/write several more bitmap font formats using an embedded version of 'monobit'.
	"""
	
	homepage = "https://trevorldavis.com/R/bittermelon/"
	cran = "bittermelon" 

	version("1.1.2", md5="75806a0748626219b04536999f1769e2")

	depends_on("r-findpython", type=("build", "run"))
	depends_on("r-png", type=("build", "run"))
	depends_on("r-rappdirs", type=("build", "run"))
	depends_on("r-unicode", type=("build", "run"))
