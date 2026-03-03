# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMixsmsn(RPackage):
	"""Fitting Finite Mixture of Scale Mixture of Skew-Normal
Distributions

	Functions to fit finite mixture of scale mixture of skew-normal (FM-SMSN) distributions, details in Prates, Lachos and Cabral (2013) <doi: 10.18637/jss.v054.i12>, Cabral, Lachos and Prates (2012) <doi:10.1016/j.csda.2011.06.026> and Basso, Lachos, Cabral and Ghosh (2010) <doi:10.1016/j.csda.2009.09.031>.
	"""
	
	cran = "mixsmsn" 

	version("1.1-10", md5="fbb96b987d5d2ed7e379a4d25d698dc0")

	depends_on("r@1.9:", type=("build", "run"))
	depends_on("r-mvtnorm@0.9.9:", type=("build", "run"))
