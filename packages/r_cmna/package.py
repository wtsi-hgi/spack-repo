# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCmna(RPackage):
	"""Computational Methods for Numerical Analysis

	Provides the source and examples for James P. Howard, II, 
             "Computational Methods for Numerical Analysis with R," 
             <https://jameshoward.us/cmna/>, a book on numerical
             methods in R.
	"""
	
	homepage = "https://jameshoward.us/cmna/"
	cran = "cmna" 

	version("1.0.5", md5="03b0945df803479bc8d88322e58e18a4")

	depends_on("r@2.10:", type=("build", "run"))
