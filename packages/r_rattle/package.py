# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRattle(RPackage):
	"""Graphical User Interface for Data Science in R

	The R Analytic Tool To Learn Easily (Rattle) provides a 
  collection of utilities functions for the data scientist. A
  Gnome (RGtk2) based graphical interface is included with 
  the aim to provide a simple and intuitive introduction to R 
  for data science, allowing a user to quickly load data from a CSV file 
  (or via ODBC), transform and explore the data, 
  build and evaluate models, and export models as PMML (predictive
  modelling markup language) or as scores. A key aspect of the GUI
  is that all R commands are logged and commented through the log tab.
  This can be saved as a standalone R script file and as
  an aid for the user to 
  learn R or to copy-and-paste directly into R itself.
  Note that RGtk2 and cairoDevice have been archived on CRAN.
  See <https://rattle.togaware.com> for installation instructions.
	"""
	
	homepage = "https://rattle.togaware.com/"
	cran = "rattle" 

	version("5.5.1", md5="a1f90a61eec58836476d0fd1fb7bdb3b")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-bitops", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
	depends_on("r-rpart-plot", type=("build", "run"))
