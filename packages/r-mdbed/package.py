# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMdbed(RPackage):
	"""Moran-Downton Bivariate Exponential Distribution

	Provides 3D plots of the Moran-Downton bivariate exponential distribution (MDBED), 
  generates bivariate random values, and also provides values of the joint and conditional PDFs and CDFs. 
  Nagao M, Kadoya M (1971) <http://hdl.handle.net/2433/124795>.
  Balakrishna N, Lai CD (2009) <doi:10.1007/b101765>.
	"""
	
	cran = "MDBED" 

	version("1.0.0", md5="0cd2629ae6f73288576e9d0f17686a12")

	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-orthopolynom", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-psych", type=("build", "run"))
