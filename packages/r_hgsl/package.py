# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHgsl(RPackage):
	"""Heterogeneous Group Square-Root Lasso

	Estimation of high-dimensional multi-response regression with heterogeneous noises under Heterogeneous group square-root Lasso penalty. For details see: Ren, Z., Kang, Y., Fan, Y. and Lv, J. (2018)<arXiv:1606.03803>.
	"""
	
	cran = "HGSL" 

	version("1.0.0", md5="6a8d92693620f119a21c6855617c96e0")

	depends_on("r@3.5:", type=("build", "run"))
