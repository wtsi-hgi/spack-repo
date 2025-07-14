# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCicero(RPackage):
	"""Predict cis-co-accessibility from single-cell chromatin accessibility data

	Cicero computes putative cis-regulatory maps from single-cell chromatin accessibility data. It also extends monocle 2 for use in chromatin accessibility data.
	"""
	
	bioc = "cicero" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/cicero_1.20.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/cicero/cicero_1.20.0.tar.gz"]

    version("1.26.0", tag="RELEASE_3_21")
	version("1.20.0", sha256="c59b4a1cb65a373646d2ffc3574f390f87afc36ac5de540bbe856472781876a7")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-monocle", type=("build", "run"))
	depends_on("r-gviz@1.22.3:", type=("build", "run"))
	depends_on("r-assertthat@0.2:", type=("build", "run"))
	depends_on("r-biobase@2.37.2:", type=("build", "run"))
	depends_on("r-biocgenerics@0.23:", type=("build", "run"))
	depends_on("r-data-table@1.10.4:", type=("build", "run"))
	depends_on("r-dplyr@0.7.4:", type=("build", "run"))
	depends_on("r-fnn@1.1:", type=("build", "run"))
	depends_on("r-genomicranges@1.30.3:", type=("build", "run"))
	depends_on("r-ggplot2@2.2.1:", type=("build", "run"))
	depends_on("r-glasso@1.8:", type=("build", "run"))
	depends_on("r-igraph@1.1:", type=("build", "run"))
	depends_on("r-iranges@2.10.5:", type=("build", "run"))
	depends_on("r-matrix@1.2.12:", type=("build", "run"))
	depends_on("r-plyr@1.8.4:", type=("build", "run"))
	depends_on("r-reshape2@1.4.3:", type=("build", "run"))
	depends_on("r-s4vectors@0.14.7:", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-stringr@1.2:", type=("build", "run"))
	depends_on("r-tibble@1.4.2:", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-vgam@1.0.5:", type=("build", "run"))
