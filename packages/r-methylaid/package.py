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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/MethylAid_1.36.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/MethylAid/MethylAid_1.36.0.tar.gz"]

	version("1.36.0", md5="8e5139726d6384208be410a794ba6388")

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
