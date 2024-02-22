# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPsgp(RPackage):
	"""Projected Spatial Gaussian Process Methods

	Implements projected sparse Gaussian process Kriging (Ingram 'et. al.', 2008, <doi:10.1007/s00477-007-0163-9>) as an additional method for the 'intamap' package. More details on implementation (Barillec 'et. al.', 2010, <doi:10.1016/j.cageo.2010.05.008>).
	"""
	
	cran = "psgp" 

	version("0.3-21", md5="a5cde717ee05ae7f140eb5c82b3b0a32")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-intamap", type=("build", "run"))
	depends_on("r-gstat", type=("build", "run"))
	depends_on("r-automap", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo@0.2:", type=("build", "run"))
