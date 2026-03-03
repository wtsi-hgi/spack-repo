# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJsparo(RPackage):
	"""Joint Sparse Optimization via Proximal Gradient Method for Cell
Fate Conversion

	Implementation of joint sparse optimization (JSparO) to infer the gene regulatory network for cell fate conversion. The proximal gradient method is implemented to solve different low-order regularization models for JSparO.
	"""
	
	cran = "JSparO" 

	version("1.5.0", md5="f5adda4f6d62048ff85a14974b5e3346")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
