# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
	
from spack.package import *
	
			
class RPpcor(RPackage):
	"""Partial and Semi-Partial (Part) Correlation

	Calculates partial and semi-partial
        (part) correlations along with p-value.
	"""
	
	cran = "ppcor" 

	version("1.1", md5="1b9b87359c7b491cfc5e4acdb2b2125a")

	depends_on("r@2.6.0:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))

