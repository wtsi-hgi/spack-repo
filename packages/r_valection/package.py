# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RValection(RPackage):
	"""Sampler for Verification Studies

	A binding for the 'valection' program which offers various ways to 
  sample the outputs of competing algorithms or parameterizations, and fairly 
  assess their performance against each other. The 'valection' C library is 
  required to use this package and can be downloaded from:
  <http://labs.oicr.on.ca/boutros-lab/software/valection>. Cooper CI, et al; Valection: Design Optimization for Validation and Verification Studies; Biorxiv 2018; <doi:10.1101/254839>.
	"""
	
	homepage = "http://labs.oicr.on.ca/boutros-lab/software/valection"
	cran = "valection" 

	version("1.0.0", md5="7c60b7ea70913d63fea3f63a61e790d0")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-testthat", type=("build", "run"))
