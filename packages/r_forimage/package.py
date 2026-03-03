# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RForimage(RPackage):
	"""Foraminiferal Image Analysis and Test Measurement

	
    The goal of this collection of functions is to provide an easy to use tool for the measurement of foraminifera and other unicellulars organisms size. With functions developed to guide foraminiferal test biovolume calculations and cell biomass estimations. The volume function includes several microalgae models geometric adaptations based on Hillebrand et al. (1999) <doi:10.1046/j.1529-8817.1999.3520403.x>, Sun and Liu (2003) <doi:10.1093/plankt/fbg096> and Vadrucci, Cabrini and Basset (2007) <doi:10.1285/i1825229Xv1n2p83>.
	"""
	
	homepage = "https://github.com/ThaiseRF/forImage"
	cran = "forImage" 

	version("0.1.0", md5="bf15fe476dabe45f12ce080cd165fca4")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-reticulate", type=("build", "run"))
	depends_on("python@3.5:", type=("build", "link", "run"))
	depends_on("py-numpy@1.18.1:", type=("build", "link", "run"))
	depends_on("py-scipy@1.4.1", type=("build", "link", "run"))
	depends_on("py-pandas@1.0.2:", type=("build", "link", "run"))
	depends_on("py-pillow@7.0.0:", type=("build", "link", "run"))
	depends_on("opencv@4.1.2:", type=("build", "link", "run"))
