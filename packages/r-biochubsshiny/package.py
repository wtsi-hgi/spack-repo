# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBiochubsshiny(RPackage):
	"""View AnnotationHub and ExperimentHub Resources Interactively

	A package that allows interactive exploration of AnnotationHub and ExperimentHub resources. It uses DT / DataTable to display resources for multiple organisms. It provides template code for reproducibility and for downloading resources via the indicated Hub package.
	"""
	
	homepage = "https://github.com/Bioconductor/BiocHubsShiny"
	bioc = "BiocHubsShiny"

	version("1.8.1", commit="166f61d62100219c80d9345a8ab9c8032d2b82b2")
	version("1.2.0", commit="ed13c4354f719102e2718b2a9179e40e32d716d7")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-annotationhub", type=("build", "run"))
	depends_on("r-experimenthub", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-shinyace", type=("build", "run"))
	depends_on("r-shinyjs", type=("build", "run"))
	depends_on("r-shinythemes", type=("build", "run"))
	depends_on("r-shinytoastr", type=("build", "run"))
