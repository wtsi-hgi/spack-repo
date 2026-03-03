# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAwesom(RPackage):
	"""Interactive Self-Organizing Maps

	Self-organizing maps (also known as SOM, see Kohonen (2001) <doi:10.1007/978-3-642-56927-2>) are a method for dimensionality reduction and clustering of continuous data. This package introduces interactive (html) graphics for easier analysis of SOM results. It also features an interactive interface, for push-button training and visualization of SOM on numeric, categorical or mixed data, as well as tools to evaluate the quality of SOM.
	"""
	
	cran = "aweSOM" 

	version("1.3", md5="88ebe0917aaa3a3094eda507bb246e20")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-kohonen@2:", type=("build", "run"))
	depends_on("r-shiny@1.6:", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-bslib", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-rclipboard", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-viridis", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-kernlab", type=("build", "run"))
	depends_on("r-fields", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-haven", type=("build", "run"))
	depends_on("r-foreign", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-readods", type=("build", "run"))
