# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSurvexpFr(RPackage):
	"""Relative Survival, AER and SMR Based on French Death Rates

	It computes Relative survival, AER and SMR based on French death rates.
	"""
	
	cran = "survexp.fr" 

	version("1.1", md5="c7f02bf1bab89ea8dbaeec8feeb930d8")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-writexls", type=("build", "run"))
