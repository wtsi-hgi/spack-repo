# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCoastlinefd(RPackage):
	"""Calculation of the Fractal Dimension of a Coastline

	Calculating the fractal dimension of a coastline using the boxes and dividers methods.
	"""
	
	homepage = "https://github.com/redworld123/CoastlineFD"
	cran = "CoastlineFD" 

	version("1.1.2", md5="cd60145aac46d7f03f12b47fc2e58bf6")

	depends_on("r-sf", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-fields", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-writexl", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-sfheaders", type=("build", "run"))
