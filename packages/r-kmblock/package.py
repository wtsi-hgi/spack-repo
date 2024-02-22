# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKmblock(RPackage):
	"""k-Means Like Blockmodeling of One-Mode and Linked Networks

	Implements k-means like blockmodeling of one-mode and linked networks as presented in Žiberna (2020) <doi:10.1016/j.socnet.2019.10.006>. The development of this package is financially supported by the Slovenian Research Agency (<https://www.arrs.si/>) within the research programs P5-0168 and the research projects J7-8279 (Blockmodeling multilevel and temporal networks) and J5-2557 (Comparison and evaluation of different approaches to blockmodeling dynamic networks by simulations with application to Slovenian co-authorship networks).
	"""
	
	cran = "kmBlock" 

	version("0.1.2", md5="fd2388a3d3948faffa581a61d0fd071a")

	depends_on("r-blockmodeling", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-dorng", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
