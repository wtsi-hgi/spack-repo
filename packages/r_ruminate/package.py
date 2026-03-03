# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRuminate(RPackage):
	"""A Pharmacometrics Data Transformation and Analysis Tool

	Exploration of pharmacometrics data involves both general tools (transformation and plotting) and specific techniques (non-compartmental analysis). This kind of exploration is generally accomplished by utilizing different packages. The purpose of 'ruminate' is to create a 'shiny' interface to make these tools more broadly available while creating reproducible results.
	"""
	
	homepage = "https://ruminate.ubiquity.tools/"
	cran = "ruminate" 

	version("0.2.2", md5="974da6d01abeb9484477a6eac92d4a0a")
	version("0.2.1", md5="7da34c5e3154d8382c1fa1b336fbbccb")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-flextable", type=("build", "run"))
	depends_on("r-formods@0.1.3:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-onbrand@1.0.3:", type=("build", "run"))
	depends_on("r-pknca@0.10.2:", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-rhandsontable", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinyace", type=("build", "run"))
	depends_on("r-shinywidgets", type=("build", "run"))
	depends_on("r-rxode2@2.1.2:", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
