# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgplotlyextra(RPackage):
	"""Extra Convenience Functions for 'Plotly'

	Convenience functions for smooth conversion from 'ggplot' to 'plotly' where the conversion using ggplotly() usually gives an unexpected labels. The package ease the process of making a 'plotly' figures generated from 'ggplot2' object more aesthetic in terms of labels and customizability. 
	"""
	
	cran = "ggplotlyExtra" 

	version("0.0.1", md5="ee2a8f7ec04dd20436aa9b89a8c8f9f0")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
