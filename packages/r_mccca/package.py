# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMccca(RPackage):
	"""Visualizing Class Specific Heterogeneous Tendencies in
Categorical Data

	Performing multiple-class cluster correspondence analysis(MCCCA). The main functions are create.MCCCAdata() to create a list to be applied to MCCCA, MCCCA() to apply MCCCA, and plot.mccca() for visualizing MCCCA result. Methods used in the 
  package refers to Mariko Takagishi and Michel van de Velden (2022)<doi:10.1080/10618600.2022.2035737>.
	"""
	
	cran = "mccca" 

	version("1.1.0.1", md5="050c6422c672b3393058eb879ac4a546")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-magic", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-wordcloud", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
