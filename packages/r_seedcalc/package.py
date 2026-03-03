# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSeedcalc(RPackage):
	"""Seed Germination and Seedling Growth Indexes

	Functions to calculate seed germination and seedling emergence and growth indexes. The main indexes for germination and seedling emergence, considering the time for seed germinate are: T10, T50 and T90, in Farooq et al. (2005) <10.1111/j.1744-7909.2005.00031.x>; and MGT, in Labouriau (1983). Considering the germination speed are: Germination Speed Index, in Maguire (1962), Mean Germination Rate, in Labouriau (1983); considering the homogeneity of germination are: Coefficient of Variation of the Germination Time, in Carvalho et al. (2005) <10.1590/S0100-84042005000300018>, and Variance of Germination, in Labouriau (1983); Uncertainty, in Labouriau and Valadares (1976) <ISSN:0001-3765>; and Synchrony, in Primack (1980). The main seedling indexes are Growth, in Sako (2001), Uniformity, in Sako (2001) and Castan et al. (2018) <doi:10.1590/1678-992x-2016-0401>; and Vigour, in Medeiros and Pereira (2018) <doi:10.1590/1983-40632018v4852340>.
	"""
	
	cran = "SeedCalc" 

	version("1.0.0", md5="d234aa6ee32b4b71a2e9106418ca6d19")

