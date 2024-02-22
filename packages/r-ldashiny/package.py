# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLdashiny(RPackage):
	"""User-Friendly Interface for Review of Scientific Literature

	Contains the development of a tool that provides a
    web-based graphical user interface (GUI) to perform a review of the
    scientific literature under the Bayesian approach of Latent Dirichlet
    Allocation (LDA)and machine learning algorithms. The application
    methodology is framed by the well known procedures in topic modelling
    on how to clean and process data. Contains methods described by 
    Blei, David M., Andrew Y. Ng, and Michael I. Jordan (2003) 
    <https://jmlr.org/papers/volume3/blei03a/blei03a.pdf> 
    Allocation"; Thomas L. Griffiths and Mark Steyvers (2004) 
    <doi:10.1073/pnas.0307752101> ; Xiong Hui, et al (2019) 
    <doi:10.1016/j.cie.2019.06.010>.
	"""
	
	cran = "LDAShiny" 

	version("0.9.3", md5="5d212ccfec43bd4e13c393ffa42e45fe")

	depends_on("r-beepr", type=("build", "run"))
	depends_on("r-broom", type=("build", "run"))
	depends_on("r-chinese-misc", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-dt@0.15:", type=("build", "run"))
	depends_on("r-highcharter", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-ldatuning", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-quanteda", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinyalert", type=("build", "run"))
	depends_on("r-shinybs", type=("build", "run"))
	depends_on("r-shinycssloaders", type=("build", "run"))
	depends_on("r-shinydashboard", type=("build", "run"))
	depends_on("r-shinyjs", type=("build", "run"))
	depends_on("r-shinywidgets", type=("build", "run"))
	depends_on("r-snowballc", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-textminer", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tidytext", type=("build", "run"))
	depends_on("r-tm", type=("build", "run"))
	depends_on("r-topicmodels", type=("build", "run"))
