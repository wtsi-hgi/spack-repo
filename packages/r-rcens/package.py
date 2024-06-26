# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcens(RPackage):
	"""Generate Sample Censoring

	Provides functions to generate censored samples of type I, II and III, from any random sample generator. It also supplies the option to create left and right censorship. Along with this, the generation of samples with interval censoring is in the  testing phase, with two options of fixed length intervals and random lengths.
	"""
	
	homepage = "https://github.com/dlsaavedra/rcens"
	cran = "rcens" 

	version("0.1.1", md5="f7469dd765dc935ee3dd9b591a571da4")

