# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUmp(RPackage):
	"""Uniformly Most Powerful Tests

	Does uniformly most powerful (UMP) and uniformly most
    powerful unbiased (UMPU) tests.  At present only distribution implemented
    is binomial distribution.  Also does fuzzy tests and confidence intervals
    (following Geyer and Meeden, 2005, <doi:10.1214/088342305000000340>)
    for the binomial
    distribution (one-tailed procedures based on UMP test and two-tailed
    procedures based on UMPU test).
	"""
	
	homepage = "http://www.stat.umn.edu/geyer/fuzz/"
	cran = "ump" 

	version("0.5-8", md5="5275bfd51aa78525d5e5e163c6b0afc6")

	depends_on("r@3.0.2:", type=("build", "run"))
