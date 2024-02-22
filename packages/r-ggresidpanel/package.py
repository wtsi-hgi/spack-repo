# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgresidpanel(RPackage):
	"""Panels and Interactive Versions of Diagnostic Plots using
'ggplot2'

	An R package for creating panels of diagnostic plots for residuals from a model 
    using ggplot2 and plotly to analyze residuals and model assumptions from a variety of 
    viewpoints. It also allows for the creation of interactive diagnostic plots.
	"""
	
	homepage = "https://goodekat.github.io/ggResidpanel/"
	cran = "ggResidpanel" 

	version("0.3.0", md5="f75f16685adff67acca11f668fa90009")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-qqplotr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
