# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClast(RPackage):
	"""Exact Confidence Limits after a Sequential Trial

	The user first provides design vectors n, a and b as well as null (p0) and alternative (p1) benchmark values for the probability of success. The key function "mv.plots.SM()" calculates mean values of exact upper and lower limits based on four different rank ordering methods. These plots form the basis of selecting a rank ordering. The function "inference()" calculates exact limits from a provided realisation and ordering choice. For more information, see "Exact confidence limits after a group sequential single arm binary trial" by Lloyd, C.J. (2020), Statistics in Medicine, Volume 38, 2389-2399, <doi:10.1002/sim.8909>.
	"""
	
	cran = "CLAST" 

	version("1.0.1", md5="2f98cb39e847c5188e7c648f393aa64d")

	depends_on("r@3.2:", type=("build", "run"))
