# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSopc(RPackage):
	"""The Sparse Online Principal Component Estimation Algorithm

	The sparse online principal component can not only process the online data set, but also obtain a sparse solution of the online data set. The philosophy of the package is described in Guo G. (2022) <doi:10.1007/s00180-022-01270-z>.
	"""
	
	cran = "SOPC" 

	version("0.1.0", md5="89493c1852eeb0016a67f9a1c58f99ea")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-elasticnet", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
