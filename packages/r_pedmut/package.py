# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPedmut(RPackage):
	"""Mutation Models for Pedigree Likelihood Computations

	A collection of functions for modelling mutations in
    pedigrees with marker data, as used e.g. in likelihood computations
    with microsatellite data. Implemented models include equal,
    proportional and stepwise models, as well as random models for
    experimental work, and custom models allowing the user to apply any
    valid mutation matrix. Allele lumping is done following the
    lumpability criteria of Kemeny and Snell (1976), ISBN:0387901922.
	"""
	
	homepage = "https://github.com/magnusdv/pedmut"
	cran = "pedmut" 

	version("0.7.1", md5="259f707573cd7ac888dffb14fd2e40fd")

	depends_on("r@4.1:", type=("build", "run"))
