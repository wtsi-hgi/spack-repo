# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFdasp(RPackage):
	"""Sparse Functional Data Analysis Methods

	Provides algorithms to fit linear regression models under several popular penalization techniques and functional linear regression models based on Majorizing-Minimizing (MM) and Alternating Direction Method of Multipliers (ADMM) techniques.
    See Boyd et al (2010) <doi:10.1561/2200000016> for complete introduction to the method.
	"""
	
	cran = "fdaSP" 

	version("1.1.1", md5="62b0f25b69ee3965541249f7a67d106a")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-ks", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
