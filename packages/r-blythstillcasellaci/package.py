# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBlythstillcasellaci(RPackage):
	"""Blyth-Still-Casella Exact Binomial Confidence Intervals

	Computes Blyth-Still-Casella exact binomial confidence intervals based on a refining procedure proposed by George Casella (1986) <doi:10.2307/3314658>. 
	"""
	
	cran = "BlythStillCasellaCI" 

	version("1.0.0", md5="b5f0953e47371e452470e5690706dceb")

	depends_on("r@3.2:", type=("build", "run"))
