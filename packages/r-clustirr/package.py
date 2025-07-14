# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClustirr(RPackage):
	"""Clustering of immune receptor repertoires

	ClustIRR is a quantitative method for clustering of immune receptor repertoires (IRRs). The algorithm identifies groups of T or B cell receptors (TCRs or BCRs) with similar specificity by comparing their sequences. ClustIRR uses graphs to visualize the specificity structures of IRRs.
	"""
	
	homepage = "https://github.com/snaketron/ClustIRR"
	bioc = "ClustIRR" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/ClustIRR_1.0.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/ClustIRR/ClustIRR_1.0.0.tar.gz"]

	version("1.6.0", tag="RELEASE_3_21")
	version("1.0.0", sha256="f54c2788eed171e691476b2113665749eb5880c10c138aec71f07577f135b8e7")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-stringdist", type=("build", "run"))
	depends_on("r-future", type=("build", "run"))
	depends_on("r-future-apply", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-visnetwork", type=("build", "run"))
