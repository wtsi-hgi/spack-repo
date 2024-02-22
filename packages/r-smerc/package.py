# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSmerc(RPackage):
	"""Statistical Methods for Regional Counts

	Implements statistical methods for analyzing the counts of areal data, with a focus on the detection of spatial clusters and clustering.  The package has a heavy emphasis on spatial scan methods, which were first introduced by Kulldorff and Nagarwalla (1995) <doi:10.1002/sim.4780140809> and Kulldorff (1997) <doi:10.1080/03610929708831995>.
	"""
	
	cran = "smerc" 

	version("1.8.3", md5="1d545de518b62abd93c8e513d5bc27a7")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppprogress", type=("build", "run"))
