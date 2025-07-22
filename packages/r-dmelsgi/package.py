# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDmelsgi(RPackage):
	"""Experimental data and documented source code for the paper "A Map of Directional Genetic Interactions in a Metazoan Cell"

	The package contains the experimental data and documented source code of the manuscript "Fischer et al., A Map of Directional Genetic Interactions in a Metazoan Cell, eLife, 2015, in Press.". The vignette code generates all figures in the paper.
	"""
	
	bioc = "DmelSGI" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/DmelSGI_1.34.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/DmelSGI/DmelSGI_1.34.0.tar.gz"]

	version("1.34.0", sha256="29a4cf80b7b8688c4ef615b30a4b54e815b09ae689cffcb2f3e0009be5e15be3")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-tsp", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-rhdf5", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))

