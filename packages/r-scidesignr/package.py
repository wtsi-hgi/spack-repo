# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScidesignr(RPackage):
	"""Data Sets from Design and Analysis of Experiments and
Observational Studies using R

	Data used in Taback, N. (2022). Design and Analysis of Experiments and Observational Studies using R. Chapman & Hall/CRC.
	"""
	
	cran = "scidesignR" 

	version("1.0.0", md5="a33c533f5f4f4b7ed3ee18ba6b12a9bf")

	depends_on("r@3.5:", type=("build", "run"))
