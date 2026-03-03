# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGwasexacthw(RPackage):
	"""Exact Hardy-Weinburg Testing for Genome Wide Association Studies

	
  Exact Hardy-Weinburg testing (using Fisher's test) for SNP genotypes
  as typically obtained in a Genome Wide Association Study (GWAS).
	"""
	
	cran = "GWASExactHW" 

	version("1.2", md5="717c13915dbf0c689722e43f98d25f96")
	version("1.01", md5="041fc38bed5b43e6f81962b872cbfbe4")

