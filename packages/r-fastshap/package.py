# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFastshap(RPackage):
	"""Fast Approximate Shapley Values

	Computes fast (relative to other implementations) approximate 
    Shapley values for any supervised learning model. Shapley values help to 
    explain the predictions from any black box model using ideas from game 
    theory; see Strumbel and Kononenko (2014) <doi:10.1007/s10115-013-0679-x> 
    for details.
	"""
	
	homepage = "https://github.com/bgreenwell/fastshap"
	cran = "fastshap" 

	version("0.1.0", md5="78f9017f02a54de5c2a78431f1419d27")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
