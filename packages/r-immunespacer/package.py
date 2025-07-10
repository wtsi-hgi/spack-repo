# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RImmunespacer(RPackage):
	"""A Thin Wrapper around the ImmuneSpace Data and Tools Portal

	Provides a convenient API for accessing data sets within ImmuneSpace Data and Tools Portal (datatools.immunespace.org), the data repository and analysis platform of the Human Immunology Project Consortium (HIPC).
	"""
	
	homepage = "https://github.com/RGLab/ImmuneSpaceR"
	bioc = "ImmuneSpaceR" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/ImmuneSpaceR_1.30.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/ImmuneSpaceR/ImmuneSpaceR_1.30.0.tar.gz"]

	version("1.30.0", sha256="c7225c047d735e5f2169e6902c288961a54a297866916ef16681fb4e60a61152")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-rlabkey@2.3.1:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-pheatmap", type=("build", "run"))
	depends_on("r-ggplot2@3.2:", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-heatmaply@0.7:", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-preprocesscore", type=("build", "run"))
	depends_on("r-flowcore", type=("build", "run"))
	depends_on("r-flowworkspace", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
