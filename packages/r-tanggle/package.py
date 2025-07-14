# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTanggle(RPackage):
	"""Visualization of Phylogenetic Networks

	Offers functions for plotting split (or implicit) networks (unrooted, undirected) and explicit networks (rooted, directed) with reticulations extending. 'ggtree' and using functions from 'ape' and 'phangorn'. It extends the 'ggtree' package [@Yu2017] to allow the visualization of phylogenetic networks using the 'ggplot2' syntax. It offers an alternative to the plot functions already available in 'ape' Paradis and Schliep (2019) <doi:10.1093/bioinformatics/bty633> and 'phangorn' Schliep (2011) <doi:10.1093/bioinformatics/btq706>.
	"""
	
	homepage = "https://klausvigo.github.io/tanggle"
	bioc = "tanggle" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/tanggle_1.8.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/tanggle/tanggle_1.8.0.tar.gz"]

	version("1.14.0", tag="RELEASE_3_21")
	version("1.8.0", sha256="10c0eaec8f0c0740189c697521297d3c99144519e45aef11fdfd56c86df1c53d")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-ggplot2@2.2:", type=("build", "run"))
	depends_on("r-ggtree", type=("build", "run"))
	depends_on("r-ape@5:", type=("build", "run"))
	depends_on("r-phangorn@2.5:", type=("build", "run"))
