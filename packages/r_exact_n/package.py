# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RExactN(RPackage):
	"""Exact Samples Sizes and Inference for Clinical Trials with
Binary Endpoint

	Allows the user to determine minimum sample sizes that achieve target size and power at a specified alternative. For more information, see “Exact samples sizes for clinical trials subject to size and power constraints” by Lloyd, C.J. (2022) Preprint <doi:10.13140/RG.2.2.11828.94085>. 
	"""
	
	cran = "exact.n" 

	version("1.1.1", md5="b5fb45597411b4cda12b2b8260775ad9")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
