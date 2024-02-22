# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCpd(RPackage):
	"""Complex Pearson Distributions

	Probability mass function, distribution function, quantile function and random generation for the Complex Triparametric Pearson (CTP) and Complex Biparametric Pearson (CBP) distributions developed by Rodriguez-Avi et al (2003) <doi:10.1007/s00362-002-0134-7>, Rodriguez-Avi et al (2004) <doi:10.1007/BF02778271> and Olmo-Jimenez et al (2018) <doi:10.1080/00949655.2018.1482897>. The package also contains maximum-likelihood fitting functions for these models.
	"""
	
	cran = "cpd" 

	version("0.3.2", md5="17b8aef03c5be5e3db77f2c3d32c2530")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-hypergeo", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-dgof", type=("build", "run"))
