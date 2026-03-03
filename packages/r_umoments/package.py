# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUmoments(RPackage):
	"""Unbiased Central Moment Estimates

	Calculates one-sample unbiased central moment estimates and 
    two-sample pooled estimates up to 6th order, including estimates of 
    powers and products of central moments. Provides the machinery for 
    obtaining unbiased central moment estimators beyond 6th order by generating
    expressions for expectations of raw sample moments and their powers and 
    products. 
    Gerlovina and Hubbard (2019) <doi:10.1080/25742558.2019.1701917>.
	"""
	
	cran = "Umoments" 

	version("0.1.1", md5="31dff718d9e0fc95cdc002726d550b99")

	depends_on("r@3.4:", type=("build", "run"))
