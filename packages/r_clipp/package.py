# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClipp(RPackage):
	"""Calculating Likelihoods by Pedigree Paring

	A fast and general implementation of the Elston-Stewart algorithm
 that can calculate the likelihoods of large and complex pedigrees. 
 References for the Elston-Stewart algorithm are
 Elston & Stewart (1971) <doi:10.1159/000152448>,
 Lange & Elston (1975) <doi:10.1159/000152714> and
 Cannings et al. (1978) <doi:10.2307/1426718>. 
	"""
	
	cran = "clipp" 

	version("1.1.1", md5="f46b1a3ceed01ae07cc659b9cb7f53dd")

	depends_on("r@3.5:", type=("build", "run"))
