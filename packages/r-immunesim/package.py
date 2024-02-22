# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RImmunesim(RPackage):
	"""Tunable Simulation of B- And T-Cell Receptor Repertoires

	Simulate full B-cell and T-cell receptor repertoires using an in silico 
    recombination process that includes a wide variety of tunable parameters to introduce noise and biases. 
    Additional post-simulation modification functions allow the user to implant motifs or codon biases as 
    well as remodeling sequence similarity architecture. The output repertoires contain records of all 
    relevant repertoire dimensions and can be analyzed using provided repertoire analysis functions.
    Preprint is available at bioRxiv (Weber et al., 2019 <doi:10.1101/759795>).
	"""
	
	homepage = "https://immuneSIM.readthedocs.io"
	cran = "immuneSIM" 

	version("0.8.7", md5="99da31084c07bfcd7d48456b6b265bc7")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-powerlaw", type=("build", "run"))
	depends_on("r-stringdist", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggthemes", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-metrics", type=("build", "run"))
	depends_on("r-repmis", type=("build", "run"))
