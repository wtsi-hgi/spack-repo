# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTimeordered(RPackage):
	"""Time-Ordered and Time-Aggregated Network Analyses

	Approaches for incorporating time into network analysis. Methods include: construction of time-ordered networks (temporal graphs); shortest-time and shortest-path-length analyses; resource spread calculations; data resampling and rarefaction for null model construction; reduction to time-aggregated networks with variable window sizes; application of common descriptive statistics to these networks; vector clock latencies; and plotting functionalities. The package supports <doi:10.1371/journal.pone.0020298>. 
	"""
	
	cran = "timeordered" 

	version("1.0.0", md5="45f499ce62f4a04d1afc9b7281669f17")

	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
