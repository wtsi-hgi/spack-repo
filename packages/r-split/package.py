# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSplit(RPackage):
	"""Split a Dataset for Training and Testing

	Procedure to optimally split a dataset for training and testing. 
    'SPlit' is based on the method of support points, which is independent of modeling methods.
    Please see Joseph and Vakayil (2021) <doi:10.1080/00401706.2021.1921037> for details.
    This work is supported by U.S. National Science Foundation grant DMREF-1921873.
	"""
	
	cran = "SPlit" 

	version("1.2", md5="f9ece635e41ab8e73b1b8931efd135fb")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
