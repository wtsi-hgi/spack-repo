# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDerfinderplot(RPackage):
	"""Plotting functions for derfinder

	This package provides plotting functions for results from the derfinder package. This helps separate the graphical dependencies required for making these plots from the core functionality of derfinder.
	"""
	
	homepage = "https://github.com/leekgroup/derfinderPlot"
	bioc = "derfinderPlot" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/derfinderPlot_1.36.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/derfinderPlot/derfinderPlot_1.36.0.tar.gz"]

	version("1.42.0", tag="RELEASE_3_21")
	version("1.36.0", sha256="8f29517009458968811b9f619a3ec9e11fe2e26c5e4f17abf7efb120fb6ef6cf")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-derfinder@1.1:", type=("build", "run"))
	depends_on("r-genomeinfodb@1.3.3:", type=("build", "run"))
	depends_on("r-genomicfeatures", type=("build", "run"))
	depends_on("r-genomicranges@1.17.40:", type=("build", "run"))
	depends_on("r-ggbio@1.13.13:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-iranges@1.99.28:", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-s4vectors@0.9.38:", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
