# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLavacvxr(RPackage):
	"""Lava Estimation for the Sum of Sparse and Dense Signals(3
Methods)

	The lava estimation is used to recover signals that is the sum of a sparse signal and a dense signal. The post-lava method corrects the shrinkage bias of lava. For more information on the lava estimation, see Chernozhukov, Hansen, and Liao (2017) <doi:10.1214/16-AOS1434>.
	"""
	
	cran = "LavaCvxr" 

	version("1.0.2", md5="3bee817b30cfc96cd3f82591570ba18e")

	depends_on("r-lavash", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-cvxr", type=("build", "run"))
