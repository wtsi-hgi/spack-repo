# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSparsevfc(RPackage):
	"""Sparse Vector Field Consensus for Vector Field Learning

	The sparse vector field consensus 
		(SparseVFC) algorithm (Ma et al., 2013 <doi:10.1016/j.patcog.2013.05.017>) for robust vector 
		field learning. Largely translated from the Matlab functions in <https://github.com/jiayi-ma/VFC>.
	"""
	
	homepage = "https://github.com/Sciurus365/SparseVFC"
	cran = "SparseVFC" 

	version("0.1.2", md5="2a81e61da065f1ffdd0120e92e99594a")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-pdist", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
