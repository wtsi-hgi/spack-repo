# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIfmcdm(RPackage):
	"""Intuitionistic Fuzzy Multi-Criteria Decision Making Methods

	Implementation of two multi-criteria decision making methods (MCDM): Intuitionistic Fuzzy Synthetic Measure (IFSM) and Intuitionistic Fuzzy Technique for Order of Preference by Similarity to Ideal Solution (IFTOPSIS) for intuitionistic fuzzy data sets for multi-criteria decision making problems. References describing the methods: Jefmański (2020) <doi:10.1007/978-3-030-52348-0_4>; Jefmański, Roszkowska, Kusterka-Jefmańska (2021) <doi:10.3390/e23121636>.
	"""
	
	cran = "IFMCDM" 

	version("0.1.17", md5="cbf6b602f52e49223e6170b1a6d1b3eb")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
