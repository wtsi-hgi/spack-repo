# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDimodelsvis(RPackage):
	"""Visualising and Interpreting Statistical Models Fit to
Compositional Data

	Statistical models fit to compositional data are often difficult to interpret due to the sum to 1 constraint on data variables. 'DImodelsVis' provides novel visualisations tools to aid with the interpretation of models fit to compositional data. All visualisations in the package are created using the 'ggplot2' plotting framework and can be extended like every other 'ggplot' object.
	"""
	
	homepage = "https://rishvish.github.io/DImodelsVis/"
	cran = "DImodelsVis" 

	version("1.0.1", md5="8fda9ae70017f60eed5fe67d37b4a263")

	depends_on("r-cli", type=("build", "run"))
	depends_on("r-dimodels@1.3.1:", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-ggfortify", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggtext@0.1.2:", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-insight", type=("build", "run"))
	depends_on("r-metr", type=("build", "run"))
	depends_on("r-pieglyph", type=("build", "run"))
	depends_on("r-plotwidgets", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
