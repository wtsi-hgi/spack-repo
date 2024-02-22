# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROpitools(RPackage):
	"""Analyzing the Opinions in a Big Text Document

	Designed for performing impact analysis of
  opinions in a digital text document (DTD). The 
  package allows a user to assess the extent to which a theme
  or subject within a document impacts the overall opinion 
  expressed in the document. The package can be applied to a wide 
  range of opinion-based DTD, including commentaries on social media
  platforms (such as 'Facebook', 'Twitter' and 'Youtube'), 
  online products reviews, and so on. 
  The utility of 'opitools' was originally demonstrated 
  in Adepeju and Jimoh (2021) <doi:10.31235/osf.io/c32qh> in the 
  assessment of COVID-19 impacts on neighbourhood policing using 
  Twitter data. Further examples can be found in the vignette of 
  the package.
	"""
	
	homepage = "https://github.com/MAnalytics/opitools"
	cran = "opitools" 

	version("1.8.0", md5="d60cb5683a468b7ae584cd5c15668961")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidytext", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-likert", type=("build", "run"))
	depends_on("r-tm", type=("build", "run"))
	depends_on("r-wordcloud2", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
