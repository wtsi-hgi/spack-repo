# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMethylaid(RPackage):
	"""Visual and interactive quality control of large Illumina DNA Methylation array data sets

	A visual and interactive web application using RStudio's shiny package. Bad quality samples are detected using sample-dependent and sample-independent controls present on the array and user adjustable thresholds. In depth exploration of bad quality samples can be performed using several interactive diagnostic plots of the quality control probes present on the array. Furthermore, the impact of any batch effect provided by the user can be explored.
	"""
	
	bioc = "MethylAid"

	version("1.42.0", commit="63538a9368b732963147a6da1bfaf8fcbb5fcf1a")
	version("1.36.0", commit="2ab1e43ddf88edb7b450f6dafe8bbef46df02420")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridbase", type=("build", "run"))
	depends_on("r-hexbin", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-minfi@1.22:", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
