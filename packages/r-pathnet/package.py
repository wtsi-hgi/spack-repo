# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPathnet(RPackage):
	"""An R package for pathway analysis using topological information

	PathNet uses topological information present in pathways and differential expression levels of genes (obtained from microarray experiment) to identify pathways that are 1) significantly enriched and 2) associated with each other in the context of differential expression. The algorithm is described in: PathNet: A tool for pathway analysis using topological information. Dutta B, Wallqvist A, and Reifman J. Source Code for Biology and Medicine 2012 Sep 24;7(1):10.
	"""
	
	bioc = "PathNet" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/PathNet_1.42.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/PathNet/PathNet_1.42.0.tar.gz"]

	version("1.42.0", sha256="fcba50e6df41aeaef25c5fbf4609e6d503114b322d6443838e1fb7149cc87ec7")

