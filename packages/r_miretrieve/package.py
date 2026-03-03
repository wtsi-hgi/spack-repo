# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMiretrieve(RPackage):
	"""miRNA Text Mining in Abstracts

	Providing tools for microRNA (miRNA) text mining. 
    miRetrieve summarizes miRNA literature by extracting, counting, and 
    analyzing miRNA names, thus aiming at gaining biological insights into a 
    large amount of text within a short period of time. To do so, miRetrieve 
    uses regular expressions to extract miRNAs and tokenization to 
    identify meaningful miRNA associations. In addition, miRetrieve uses 
    the latest miRTarBase version 8.0 (Hsi-Yuan Huang et al. (2020) 
    "miRTarBase 2020: updates to the experimentally validated microRNA–target 
    interaction database" <doi:10.1093/nar/gkz896>) to display field-specific 
    miRNA-mRNA interactions. The most important functions are available as a 
    Shiny web application under <https://miretrieve.shinyapps.io/miRetrieve/>.
	"""
	
	cran = "miRetrieve" 

	version("1.3.4", md5="7da565715c1bc97d056ca04abc294712")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-dplyr@1.0.7:", type=("build", "run"))
	depends_on("r-forcats@0.5.1:", type=("build", "run"))
	depends_on("r-ggplot2@3.3.5:", type=("build", "run"))
	depends_on("r-magrittr@2.0.1:", type=("build", "run"))
	depends_on("r-openxlsx@4.2.4:", type=("build", "run"))
	depends_on("r-plotly@4.9.4.1:", type=("build", "run"))
	depends_on("r-purrr@0.3.4:", type=("build", "run"))
	depends_on("r-readr@2.0.1:", type=("build", "run"))
	depends_on("r-readxl@1.3.1:", type=("build", "run"))
	depends_on("r-rlang@0.4.11:", type=("build", "run"))
	depends_on("r-scales@1.1.1:", type=("build", "run"))
	depends_on("r-stringr@1.4:", type=("build", "run"))
	depends_on("r-textclean@0.9.3:", type=("build", "run"))
	depends_on("r-tidyr@1.1.3:", type=("build", "run"))
	depends_on("r-tidytext@0.3.1:", type=("build", "run"))
	depends_on("r-topicmodels@0.2.12:", type=("build", "run"))
	depends_on("r-wordcloud@2.6:", type=("build", "run"))
	depends_on("r-xml2@1.3.2:", type=("build", "run"))
	depends_on("r-zoo@1.8.9:", type=("build", "run"))
