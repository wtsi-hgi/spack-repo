# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGeomxworkflows(RPackage):
	"""GeoMx Digital Spatial Profiler (DSP) data analysis workflows

	Workflows for use with NanoString Technologies GeoMx Technology.  Package provides bioconductor focused workflows for leveraging existing packages (e.g. GeomxTools) to process, QC, and analyze the data.
	"""
	
	bioc = "GeoMxWorkflows" 
	urls = ["https://www.bioconductor.org/packages/3.18/workflows/src/contrib/GeoMxWorkflows_1.8.0.tar.gz", "https://www.bioconductor.org/packages/3.18/workflows/src/contrib/Archive/GeoMxWorkflows/GeoMxWorkflows_1.8.0.tar.gz"]

    version("1.14.0", tag="RELEASE_3_21")
	version("1.8.0", sha256="63f8f7147a90ef44e3d02f5c01252fff9f02a2d22f05e1f22ef4770bc0dab4ed")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-nanostringnctools", type=("build", "run"))
	depends_on("r-geomxtools", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-rjson", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-envstats", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-outliers", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-ggforce", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-umap", type=("build", "run"))
	depends_on("r-rtsne", type=("build", "run"))
	depends_on("r-pheatmap", type=("build", "run"))
	depends_on("r-biocstyle", type=("build", "run"))

