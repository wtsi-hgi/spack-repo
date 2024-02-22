# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNetcontrol(RPackage):
	"""Control Theory Methods for Networks

	Implementations of various control theory methods for use 
            in brain and psychological networks. Contains controllability
            statistics from Pasqualetti, Zampieri & Bullo (2014) <doi:10.1109/TCNS.2014.2310254>,
            optimal control algorithms from Lewis, Vrabie & Syrmos (2012, ISBN:978-0-470-63349-6), and various utilities.
	"""
	
	cran = "netcontrol" 

	version("0.1", md5="f5c1446a9521b6ec1f2a71be2dfb17ca")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-expm", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
