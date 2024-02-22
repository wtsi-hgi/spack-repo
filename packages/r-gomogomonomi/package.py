# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGomogomonomi(RPackage):
	"""Animate Text using the 'Animate.css' Library

	Allows the user to animate text within 'rmarkdown' documents and 'shiny' applications. 
    The animations are activated using the 'Animate.css' library. See <https://animate.style/> for more information.
	"""
	
	homepage = "https://github.com/feddelegrand7/GomoGomonoMi"
	cran = "GomoGomonoMi" 

	version("0.1.0", md5="ff84f0bbb62ad24936296119fe723cf1")

	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
