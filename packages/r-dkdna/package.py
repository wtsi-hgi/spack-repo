# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDkdna(RPackage):
	"""Diffusion Kernels on a Set of Genotypes

	Compute diffusion kernels on DNA polymorphisms, including SNP and bi-allelic genotypes. 
	"""
	
	homepage = "http://morotalab.org/"
	cran = "dkDNA" 

	version("0.1.1", md5="ea5a0b6ae7bf37eb1fb1b8ed68c70b74")

