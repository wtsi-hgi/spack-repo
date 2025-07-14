# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCimice(RPackage):
	"""CIMICE-R: (Markov) Chain Method to Inferr Cancer Evolution

	CIMICE is a tool in the field of tumor phylogenetics and its goal is to build a Markov Chain (called Cancer Progression Markov Chain, CPMC) in order to model tumor subtypes evolution. The input of CIMICE is a Mutational Matrix, so a boolean matrix representing altered genes in a collection of samples. These samples are assumed to be obtained with single-cell DNA analysis techniques and the tool is specifically written to use the peculiarities of this data for the CMPC construction.
	"""
	
	homepage = "https://github.com/redsnic/CIMICE"
	bioc = "CIMICE" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/CIMICE_1.10.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/CIMICE/CIMICE_1.10.0.tar.gz"]

    version("1.16.0", tag="RELEASE_3_21")
	version("1.10.0", sha256="b36e7c273a36cdb9a966808543cd21836d02099ad8ec04cc1274dfc7b1974b58")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-networkd3", type=("build", "run"))
	depends_on("r-visnetwork", type=("build", "run"))
	depends_on("r-ggcorrplot", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-ggraph", type=("build", "run"))
	depends_on("r-maftools", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-tidygraph", type=("build", "run"))
	depends_on("r-expm", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
