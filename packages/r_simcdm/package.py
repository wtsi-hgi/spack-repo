# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSimcdm(RPackage):
	"""Simulate Cognitive Diagnostic Model ('CDM') Data

	Provides efficient R and 'C++' routines to simulate cognitive diagnostic
    model data for Deterministic Input, Noisy "And" Gate ('DINA') and
    reduced Reparameterized Unified Model ('rRUM') from 
    Culpepper and Hudson (2017) <doi: 10.1177/0146621617707511>,
    Culpepper (2015) <doi:10.3102/1076998615595403>, and
    de la Torre (2009) <doi:10.3102/1076998607309474>.
	"""
	
	homepage = "https://tmsalab.github.io/simcdm/"
	cran = "simcdm" 

	version("0.1.2", md5="b8a795791d02fc058226720ae7983c22")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo@0.12.6.6:", type=("build", "run"))
