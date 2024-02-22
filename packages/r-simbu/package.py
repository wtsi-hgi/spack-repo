# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSimbu(RPackage):
	"""Simulate Bulk RNA-seq Datasets from Single-Cell Datasets

	SimBu can be used to simulate bulk RNA-seq datasets with known cell type fractions. You can either use your own single-cell study for the simulation or the sfaira database. Different pre-defined simulation scenarios exist, as are options to run custom simulations. Additionally, expression values can be adapted by adding an mRNA bias, which produces more biologically relevant simulations.
	"""
	
	homepage = "https://github.com/omnideconv/SimBu"
	bioc = "SimBu" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/SimBu_1.4.3.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/SimBu/SimBu_1.4.3.tar.gz"]

	version("1.4.3", md5="f58aadeded253be20ac1d30d861501d3")

	depends_on("r-basilisk", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-matrix@1.3.3:", type=("build", "run"))
	depends_on("r-phyloseq", type=("build", "run"))
	depends_on("r-proxyc", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
	depends_on("r-reticulate", type=("build", "run"))
	depends_on("r-sparsematrixstats", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
