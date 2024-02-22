# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShinychakraslider(RPackage):
	"""Combined Slider and Numeric Input for 'Shiny'

	Provides a combined slider and numeric input for usage in a 'Shiny' app. The slider and the numeric input are linked together: each one is updated when the other one changes. Many styling properties are customizable (e.g. colors and size).
	"""
	
	homepage = "https://github.com/stla/shinyChakraSlider"
	cran = "shinyChakraSlider" 

	version("0.1.0", md5="e7349c05da34b84a88cfc089f8910ff4")

	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-reactr", type=("build", "run"))
