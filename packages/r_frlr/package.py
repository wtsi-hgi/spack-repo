# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFrlr(RPackage):
	"""Fit Repeated Linear Regressions

	When fitting a set of linear regressions which have some same variables, we can separate the matrix and reduce the computation cost. This package aims to fit a set of repeated linear regressions faster. More details can be found in this blog Lijun Wang (2017) <https://stats.hohoweiya.xyz/regression/2017/09/26/An-R-Package-Fit-Repeated-Linear-Regressions/>.
	"""
	
	homepage = "https://github.com/szcf-weiya/fRLR"
	cran = "fRLR" 

	version("1.3.0", md5="7ce93295573728ff80faf51dd7e90b7c")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("gsl", type=("build", "link", "run"))
