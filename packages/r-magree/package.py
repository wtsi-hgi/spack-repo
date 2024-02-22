# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMagree(RPackage):
	"""Implements the O'Connell-Dobson-Schouten Estimators of Agreement
for Multiple Observers

	Implements an interface to the legacy Fortran code from O'Connell and Dobson (1984) <DOI:10.2307/2531148>. Implements Fortran 77 code for the methods developed by Schouten (1982) <DOI:10.1111/j.1467-9574.1982.tb00774.x>. Includes estimates of average agreement for each observer and average agreement for each subject.
	"""
	
	cran = "magree" 

	version("1.2", md5="5d420350fe2be66dbe1b394d5d33c66a")

