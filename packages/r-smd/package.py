# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSmd(RPackage):
	"""Compute Standardized Mean Differences

	Computes standardized mean differences and confidence intervals for 
    multiple data types based on Yang, D., & Dalton, J. E. (2012) 
    <http://www.lerner.ccf.org/qhs/software/lib/stddiff.pdf>. 
	"""
	
	homepage = "https://bsaul.github.io/smd/"
	cran = "smd" 

	version("0.6.7", md5="87697e4883b1ec319128925821d39665")

	depends_on("r-mass@7.3.50:", type=("build", "run"))
