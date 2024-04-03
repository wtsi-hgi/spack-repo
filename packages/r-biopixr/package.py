# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBiopixr(RPackage):
	"""Extracting Insights from Biological Images

	Combines the 'magick' and 'imager' packages to streamline image analysis, focusing on feature extraction and quantification from biological images, especially 
    microparticles. By providing high throughput pipelines and clustering capabilities, 'biopixR' facilitates efficient insight generation for researchers (Schneider J. et al. (2019) 
    <doi:10.21037/jlpm.2019.04.05>).
	"""
	
	homepage = "https://github.com/Brauckhoff/biopixR"
	cran = "biopixR" 

	version("0.2.4", md5="f35d31b508d105b676d1b05a10cfd5e4")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-imager", type=("build", "run"))
	depends_on("r-magick", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
