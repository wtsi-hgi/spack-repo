# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgstance(RPackage):
	"""Horizontal 'ggplot2' Components

	A 'ggplot2' extension that provides flipped components:
    horizontal versions of 'Stats' and 'Geoms', and vertical versions
    of 'Positions'. This package is now superseded by 'ggplot2' itself
    which now has full native support for horizontal layouts. It
    remains available for backward compatibility.
	"""
	
	homepage = "https://github.com/lionel-/ggstance"
	cran = "ggstance" 

	version("0.3.6", md5="3ff49a13622874ce58ada9d774de9f07")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-cli@3.4.1:", type=("build", "run"))
	depends_on("r-ggplot2@3.4:", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-withr@2:", type=("build", "run"))
