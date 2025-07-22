# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBiocancer(RPackage):
	"""Interactive Multi-Omics Cancers Data Visualization and Analysis

	This package is a Shiny App to visualize and analyse interactively Multi-Assays of Cancer Genomic Data.
	"""
	
	homepage = "https://kmezhoud.github.io/bioCancer/"
	bioc = "bioCancer"

	version("1.36.0", commit="89a66db886b5bf12523a978815d620921cbf1416")
	version("1.30.8", commit="94d43a0ad9031ddeca19ba8eba30f2afb53d340d")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-radiant-data@0.9.1:", type=("build", "run"))
	depends_on("r-cbioportaldata", type=("build", "run"))
	depends_on("r-xml@3.98:", type=("build", "run"))
	depends_on("r-r-oo", type=("build", "run"))
	depends_on("r-r-methodss3", type=("build", "run"))
	depends_on("r-dt@0.3:", type=("build", "run"))
	depends_on("r-dplyr@0.7.2:", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-shiny@1.0.5:", type=("build", "run"))
	depends_on("r-algdesign@1.1.7.3:", type=("build", "run"))
	depends_on("r-import@1.1:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-shinythemes", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-genetclassifier", type=("build", "run"))
	depends_on("r-org-hs-eg-db", type=("build", "run"))
	depends_on("r-org-bt-eg-db", type=("build", "run"))
	depends_on("r-dose", type=("build", "run"))
	depends_on("r-clusterprofiler", type=("build", "run"))
	depends_on("r-reactome-db", type=("build", "run"))
	depends_on("r-reactomepa", type=("build", "run"))
	depends_on("r-diagrammer@:1.1", type=("build", "run"))
	depends_on("r-visnetwork", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-go-db", type=("build", "run"))
