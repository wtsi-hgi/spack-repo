# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROpusminer(RPackage):
	"""OPUS Miner Algorithm for Filtered Top-k Association Discovery

	Provides a simple R interface to the OPUS Miner algorithm (implemented in C++) for finding the top-k productive, non-redundant itemsets from transaction data.  The OPUS Miner algorithm uses the OPUS search algorithm to efficiently discover the key associations in transaction data, in the form of self-sufficient itemsets, using either leverage or lift.  See <http://i.giwebb.com/index.php/research/association-discovery/> for more information in relation to the OPUS Miner algorithm.
	"""
	
	cran = "opusminer" 

	version("0.1-1", md5="1c20a849a5773cec5901d1f5c8fb8408")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-arules@1.5.0:", type=("build", "run"))
	depends_on("r-matrix@1.2.7:", type=("build", "run"))
