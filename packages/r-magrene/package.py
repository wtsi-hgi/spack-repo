# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMagrene(RPackage):
	"""Motif Analysis In Gene Regulatory Networks

	magrene allows the identification and analysis of graph motifs in (duplicated) gene regulatory networks (GRNs), including lambda, V, PPI V, delta, and bifan motifs. GRNs can be tested for motif enrichment by comparing motif frequencies to a null distribution generated from degree-preserving simulated GRNs. Motif frequencies can be analyzed in the context of gene duplications to explore the impact of small-scale and whole-genome duplications on gene regulatory networks. Finally, users can calculate interaction similarity for gene pairs based on the Sorensen-Dice similarity index.
	"""
	
	homepage = "https://github.com/almeidasilvaf/magrene"
	bioc = "magrene"

	version("1.10.0", commit="899f1022c5e1ca2ecc353c0ca29decb6f8f2df2c")
	version("1.4.0", commit="268c10663ac8b7863484e3c854a0bf55723a6acb")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
