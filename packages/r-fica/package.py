# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFica(RPackage):
	"""Classical, Reloaded and Adaptive FastICA Algorithms

	Algorithms for classical symmetric and deflation-based FastICA, reloaded deflation-based FastICA algorithm and an algorithm for adaptive deflation-based FastICA using multiple nonlinearities. For details, see Miettinen et al. (2014) <doi:10.1109/TSP.2014.2356442> and Miettinen et al. (2017) <doi:10.1016/j.sigpro.2016.08.028>. The package is described in Miettinen, Nordhausen and Taskinen (2018) <doi:10.32614/RJ-2018-046>.
	"""
	
	cran = "fICA" 

	version("1.1-2", md5="712fbbbe77d88103f4c692897e7af26d")

	depends_on("r-jade", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
