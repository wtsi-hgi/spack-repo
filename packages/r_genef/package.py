# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGenef(RPackage):
	"""Package for Generalized F-Statistics

	Implementation of several generalized F-statistics. The
    current version includes a generalized F-statistic based on the
    flexible isotonic/monotonic regression or order restricted hypothesis
    testing. Based on: Y. Lai (2011) <doi:10.1371/journal.pone.0019754>.
	"""
	
	cran = "GeneF" 

	version("1.0.1", md5="e1aad4ce2f6cc6175b5f1bc4d100b469")

