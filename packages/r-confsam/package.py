# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RConfsam(RPackage):
	"""Estimates and Bounds for the False Discovery Proportion, by
Permutation

	For multiple testing.
    Computes estimates and confidence bounds for the
    False Discovery Proportion (FDP), the fraction of false positives among
    all rejected hypotheses.
    The methods in the package use permutations of the data. Doing so, they
    take into account the dependence structure in the data.
	"""
	
	cran = "confSAM" 

	version("0.2", md5="20b9fde94848e21d5fb7366e9287aba0")

