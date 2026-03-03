# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REasyalluvial(RPackage):
	"""Generate Alluvial Plots with a Single Line of Code

	Alluvial plots are similar to sankey diagrams and visualise categorical data 
    over multiple dimensions as flows. (Rosvall M, Bergstrom CT (2010) Mapping Change in 
    Large Networks. PLoS ONE 5(1): e8694. <doi:10.1371/journal.pone.0008694> 
    Their graphical grammar however is a bit more complex then that of a regular x/y 
    plots. The 'ggalluvial' package made a great job of translating that grammar into 
    'ggplot2' syntax and gives you many options to tweak the appearance of an alluvial 
    plot, however there still remains a multi-layered complexity that makes it difficult
    to use 'ggalluvial' for explorative data analysis. 'easyalluvial' provides a simple 
    interface to this package that allows you to produce a decent alluvial plot from any 
    dataframe in either long or wide format from a single line of code while also handling 
    continuous data. It is meant to allow a quick visualisation of entire dataframes 
    with a focus on different colouring options that can make alluvial plots a great 
    tool for data exploration. 
	"""
	
	homepage = "https://github.com/erblast/easyalluvial/"
	cran = "easyalluvial" 

	version("0.3.2", md5="dab556831dcc1cb6b04aae9fbaadde57")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-tidyr@1:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-ggalluvial@0.9.1:", type=("build", "run"))
	depends_on("r-ggplot2@3.2:", type=("build", "run"))
	depends_on("r-ggridges", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-recipes@0.1.5:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
	depends_on("r-progressr", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
