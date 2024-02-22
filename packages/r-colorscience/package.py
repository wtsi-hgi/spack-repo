# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RColorscience(RPackage):
	"""Color Science Methods and Data

	Methods and data for color science - color conversions by observer,
        illuminant, and gamma. Color matching functions and chromaticity diagrams.
        Color indices, color differences, and spectral data conversion/analysis.
	"""
	
	cran = "colorscience" 

	version("1.0.8", md5="a31f175a4fb9978a1a2cc2ad286f5234")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
