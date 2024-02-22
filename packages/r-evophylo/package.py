# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REvophylo(RPackage):
	"""Pre- And Postprocessing of Morphological Data from Relaxed Clock
Bayesian Phylogenetics

	Performs automated morphological character partitioning for 
             phylogenetic analyses and analyze macroevolutionary parameter 
             outputs from clock (time-calibrated) Bayesian inference analyses, following 
             concepts introduced by Simões and Pierce (2021) <doi:10.1038/s41559-021-01532-x>.
	"""
	
	homepage = "https://github.com/tiago-simoes/EvoPhylo"
	cran = "EvoPhylo" 

	version("0.3.2", md5="0731092efd0f541eef6f5c39751e5eb0")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-ape@1.16.2:", type=("build", "run"))
	depends_on("r-dplyr@1.0.8:", type=("build", "run"))
	depends_on("r-cluster@2.1.2:", type=("build", "run"))
	depends_on("r-deeptime@0.2:", type=("build", "run"))
	depends_on("r-ggplot2@3.3.5:", type=("build", "run"))
	depends_on("r-ggrepel@0.9.1:", type=("build", "run"))
	depends_on("r-ggtree@3.1.5.902:", type=("build", "run"))
	depends_on("r-patchwork", type=("build", "run"))
	depends_on("r-treeio@1.16.2:", type=("build", "run"))
	depends_on("r-rtsne@0.15:", type=("build", "run"))
	depends_on("r-unglue@0.1:", type=("build", "run"))
	depends_on("r-devtools@2.4.3:", type=("build", "run"))
