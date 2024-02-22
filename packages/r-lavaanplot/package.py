# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLavaanplot(RPackage):
	"""Path Diagrams for 'Lavaan' Models via 'DiagrammeR'

	Plots path diagrams from models in 'lavaan' using the plotting
    functionality from the 'DiagrammeR' package. 'DiagrammeR' provides nice path diagrams 
    via 'Graphviz', and these functions make it easy to generate these diagrams from a
    'lavaan' path model without having to write the DOT language graph specification.
	"""
	
	homepage = "https://github.com/alishinski/lavaanPlot"
	cran = "lavaanPlot" 

	version("0.8.1", md5="63951fbf135e7a4d1fe74ee3ef79f339")

	depends_on("r-lavaan", type=("build", "run"))
	depends_on("r-diagrammer", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
