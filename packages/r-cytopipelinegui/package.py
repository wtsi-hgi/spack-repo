# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCytopipelinegui(RPackage):
	"""GUI's for visualization of flow cytometry data analysis pipelines

	This package is the companion of the `CytoPipeline` package. It provides GUI's (shiny apps) for the visualization of flow cytometry data analysis pipelines that are run with `CytoPipeline`. Two shiny applications are provided, i.e. an interactive flow frame assessment and comparison tool and an interactive scale transformations visualization and adjustment tool.
	"""
	
	bioc = "CytoPipelineGUI" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/CytoPipelineGUI_1.0.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/CytoPipelineGUI/CytoPipelineGUI_1.0.0.tar.gz"]

	version("1.6.0", tag="RELEASE_3_21")
	version("1.0.0", sha256="18c568b019b283ba117d278606c02db621b389dd5a5494699643f109064ad925")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-cytopipeline", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-flowcore", type=("build", "run"))
