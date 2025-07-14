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

	version("1.16.0", commit="b122b6f2112e72884616ec108755cae0c7de773f")
	version("1.10.0", commit="ff02f0ed1f5bbac0545d9cae69fe22dfbbc61903")

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
