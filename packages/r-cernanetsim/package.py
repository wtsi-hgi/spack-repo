# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCernanetsim(RPackage):
	"""Regulation Simulator of Interaction between miRNA and Competing RNAs (ceRNA)

	This package simulates regulations of ceRNA (Competing Endogenous) expression levels after a expression level change in one or more miRNA/mRNAs. The methodolgy adopted by the package has potential to incorparate any ceRNA (circRNA, lincRNA, etc.) into miRNA:target interaction network.  The package basically distributes miRNA expression over available ceRNAs where each ceRNA attracks miRNAs proportional to its amount. But, the package can utilize multiple parameters that modify miRNA effect on its target (seed type, binding energy, binding location, etc.).  The functions handle the given dataset as graph object and the processes progress via edge and node variables.
	"""
	
	homepage = "https://github.com/selcenari/ceRNAnetsim"
	bioc = "ceRNAnetsim" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/ceRNAnetsim_1.14.1.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/ceRNAnetsim/ceRNAnetsim_1.14.1.tar.gz"]

	version("1.14.1", md5="38362ee61086011866cbde80da6ef5e9")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidygraph", type=("build", "run"))
	depends_on("r-furrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggraph", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-future", type=("build", "run"))
