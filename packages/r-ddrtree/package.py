# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDdrtree(RPackage):
	"""Learning Principal Graphs with DDRTree

	Provides an implementation of the framework of reversed graph embedding (RGE) which projects data into a reduced dimensional space while constructs a principal tree which passes through the middle of the data simultaneously. DDRTree shows superiority to alternatives (Wishbone, DPT) for inferring the ordering as well as the intrinsic structure of the single cell genomics data. In general, it could be used to reconstruct the temporal progression as well as bifurcation structure of any datatype. 
	"""
	
	cran = "DDRTree" 

	version("0.1.5", md5="b9970fe30d198db164d071f87abd17a5")

	depends_on("r-irlba", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
