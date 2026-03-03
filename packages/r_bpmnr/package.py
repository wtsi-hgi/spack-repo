# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBpmnr(RPackage):
	"""Support for BPMN (Business Process Management Notation) Models

	Creating, rendering and writing BPMN diagrams <https://www.bpmn.org/>. Functionalities can be used to visualize and export BPMN diagrams created using the 'pm4py' and 'bupaRminer' packages. Part of the 'bupaR' ecosystem. 
	"""
	
	cran = "bpmnR" 

	version("0.1.1", md5="2e6dedba68fb0ff67a34f543ff874cab")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-diagrammer", type=("build", "run"))
	depends_on("r-diagrammersvg", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rvest", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-uuid", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-huxtable", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
