# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLefser(RPackage):
	"""R implementation of the LEfSE method for microbiome biomarker discovery

	lefser is an implementation in R of the popular "LDA Effect Size (LEfSe)" method for microbiome biomarker discovery. It uses the Kruskal-Wallis test, Wilcoxon-Rank Sum test, and Linear Discriminant Analysis to find biomarkers of groups and sub-groups.
	"""
	
	homepage = "https://github.com/waldronlab/lefser"
	bioc = "lefser" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/lefser_1.12.1.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/lefser/lefser_1.12.1.tar.gz"]

	version("1.12.1", sha256="157dbfc094dc414ae49baa7b55a3ff48d857a6bb0f189c45509c73726de4dc2b")

	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r@4:", type=("build", "run"))
	depends_on("r-coin", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
