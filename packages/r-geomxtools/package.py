# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGeomxtools(RPackage):
	"""NanoString GeoMx Tools

	Tools for NanoString Technologies GeoMx Technology. Package provides functions for reading in DCC and PKC files based on an ExpressionSet derived object.  Normalization and QC functions are also included.
	"""
	
	bioc = "GeomxTools" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/GeomxTools_3.6.2.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/GeomxTools/GeomxTools_3.6.2.tar.gz"]

	version("3.6.2", md5="233ce698fafedbd76c8eebdacc4f9c51")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-nanostringnctools", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-rjson", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-envstats", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-lmertest", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-ggally", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-seuratobject", type=("build", "run"))
