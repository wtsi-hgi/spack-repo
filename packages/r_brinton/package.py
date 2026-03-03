# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBrinton(RPackage):
	"""A Graphical EDA Tool

	An automated graphical exploratory data analysis (EDA) tool that introduces: 
  a.) wideplot graphics for exploring the structure of a dataset through a grid of variables 
      and graphic types. 
  b.) longplot graphics, which present the entire catalog of available graphics for representing 
      a particular variable using a grid of graphic types and variations on these types.
  c.) plotup function, which presents a particular graphic for a specific variable of a dataset. 
      The plotup() function also makes it possible to obtain the code used to generate the graphic, 
      meaning that the user can adjust its properties as needed.
  d.) matrixplot graphics that is a grid of a particular graphic showing bivariate relationships
      between all pairs of variables of a certain(s) type(s) in a multivariate data set.
	"""
	
	homepage = "https://sciencegraph.github.io/brinton/"
	cran = "brinton" 

	version("0.2.7", md5="b3c06a21902286768d7c36d62944afa7")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-pander", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-sm", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-ggally", type=("build", "run"))
	depends_on("r-patchwork", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
