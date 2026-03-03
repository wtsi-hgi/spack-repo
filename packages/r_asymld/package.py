# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAsymld(RPackage):
	"""Asymmetric Linkage Disequilibrium (ALD) for Polymorphic Genetic
Data

	Computes asymmetric LD measures (ALD) for multi-allelic genetic data. These measures are identical to the correlation measure (r) for bi-allelic data.
	"""
	
	cran = "asymLD" 

	version("0.1", md5="4279e0e43acafa6bed70708fda860c2e")

