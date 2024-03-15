# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcpptimer(RPackage):
	"""'Rcpp' Tic-Toc Timer with 'OpenMP' Support

	Provides 'Rcpp' bindings for 'cpptimer', a simple tic-toc timer class for benchmarking 'C++' code <https://github.com/BerriJ/cpptimer>. It's not just simple, it's blazing fast! This sleek tic-toc timer class supports overlapping timers as well as 'OpenMP' parallelism <https://www.openmp.org/>. It boasts a microsecond-level time resolution. We did not find any overhead of the timer itself at this resolution. Results (with summary statistics) are automatically passed back to 'R' as a data frame.
	"""
	
	homepage = "https://rcpptimer.berrisch.biz"
	cran = "rcpptimer" 

	version("1.0.0", md5="4060f8da9f041d6f1a5541815fc4010a")

	depends_on("r-rcpp", type=("build", "run"))
