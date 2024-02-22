# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGradientpickerd3(RPackage):
	"""Interactive Color Gradient Picker Using 'htmlwidgets' and the
Modified JS Script 'jquery-gradient-picker'

	Widget for an interactive selection and modification of a color gradient. 'gradientPickerD3' allows addition, removement and replacement of color ticks. List of numeric values will automatically translate in their corresponding tick position within the numeric range. App returns a data.frame containing tick values, colors and the positions in percent (0.0 to 1.0) for each color tick in the gradient. The original JS 'jquery-gradient-picker' was implemented by Matt Crinklaw-Vogt (nick: tantaman) <https://github.com/tantaman/>. Widget and JS modifications were done by CD. Peikert.
	"""
	
	homepage = "https://github.com/peikert/gradientPickerD3"
	cran = "gradientPickerD3" 

	version("0.1.0.0", md5="d7efac8d9589f07ace479463ef43c748", url="https://cran.r-project.org/src/contrib/gradientPickerD3_0.1.0.0.tar.gz")

	depends_on("r@3.3.1:", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
