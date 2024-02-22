# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGwasexacthw(RPackage):
	"""Exact Hardy-Weinburg testing for Genome Wide Association Studies

	This package contains a function to do exact
        Hardy-Weinburg testing (using Fisher's test) for SNP genotypes
        as typically obtained in a Genome Wide Association Study
        (GWAS).
	"""
	
	cran = "GWASExactHW" 

	version("1.01", md5="041fc38bed5b43e6f81962b872cbfbe4")

