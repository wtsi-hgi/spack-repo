# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RC3(RPackage):
	"""'C3.js' Chart Library

	Create interactive charts with the 'C3.js' <http://c3js.org/> charting library. All plot 
    types in 'C3.js' are available and include line, bar, scatter, and mixed geometry plots. Plot 
    annotations, labels and axis are highly adjustable. Interactive web based charts can be embedded 
    in R Markdown documents or Shiny web applications. 
	"""
	
	homepage = "https://github.com/mrjoh3/c3"
	cran = "c3" 

	version("0.3.0", md5="6543d9f7b070d0464652b9464c2f8889", url="https://cran.r-project.org/src/contrib/c3_0.3.0.tar.gz")

	depends_on("r@3.2.2:", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-lazyeval", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-viridis", type=("build", "run"))
