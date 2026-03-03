# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpfda(RPackage):
	"""Function-on-Scalar Regression with Group-Bridge Penalty

	Implements a group-bridge penalized function-on-scalar regression
    model proposed by Wang et al. (2020) <arXiv:2006.10163>, to simultaneously
    estimate functional coefficient and recover the local sparsity.
	"""
	
	homepage = "https://github.com/dipterix/spfda"
	cran = "spfda" 

	version("0.9.1", md5="944b9fa2a52b2a634a3e14763b1da483")

	depends_on("r-mathjaxr", type=("build", "run"))
