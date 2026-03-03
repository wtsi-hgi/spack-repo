# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQrlabelr(RPackage):
	"""Generate Machine- And Human-Readable Plot Labels for Experiments

	A no-frills open-source solution for designing plot labels affixed with QR 
    codes. It features 'EasyQrlabelr', a 'BrAPI-compliant' 'shiny' app that 
    simplifies the process of plot label design for non-R users. It builds on the 
    methods described by Wu 'et al.' (2020) <doi:10.1111/2041-210X.13405>.
	"""
	
	cran = "qrlabelr" 

	version("0.2.0", md5="f2ec7393711bb842e86e4acea3ab9aa7")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-shinybs@0.61.1:", type=("build", "run"))
	depends_on("r-argondash@0.2:", type=("build", "run"))
	depends_on("r-argonr@0.2:", type=("build", "run"))
	depends_on("r-assertthat@0.2.1:", type=("build", "run"))
	depends_on("r-bslib@0.4.2:", type=("build", "run"))
	depends_on("r-desplot@1.10:", type=("build", "run"))
	depends_on("r-dplyr@1.0.10:", type=("build", "run"))
	depends_on("r-ggplot2@3.4.2:", type=("build", "run"))
	depends_on("r-purrr@1.0.1:", type=("build", "run"))
	depends_on("r-qbms@0.9.1:", type=("build", "run"))
	depends_on("r-qrencoder@0.1:", type=("build", "run"))
	depends_on("r-raster@3.6.23:", type=("build", "run"))
	depends_on("r-reactable@0.4.3:", type=("build", "run"))
	depends_on("r-readxl@1.4.1:", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinycssloaders@1:", type=("build", "run"))
	depends_on("r-shinyjs@2.1:", type=("build", "run"))
	depends_on("r-shinywidgets@0.7.6:", type=("build", "run"))
	depends_on("r-uuid", type=("build", "run"))
