# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROrkm(RPackage):
	"""The Online Regularized K-Means Clustering Algorithm

	Algorithm of online regularized k-means to deal with online multi(single) view data.
 The philosophy of the package is described in Guo G. (2020) 
 <doi:10.1080/02331888.2020.1823979>. 
	"""
	
	cran = "ORKM" 

	version("0.7.0.0", md5="7b27a4c03219f5ee6bc1870fb6674149")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
