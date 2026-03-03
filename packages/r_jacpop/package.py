# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJacpop(RPackage):
	"""Jaccard Index for Population Structure Identification

	Uses the Jaccard similarity index to account for population
    structure in sequencing studies. This method was specifically
    designed to detect population stratification based on rare variants, hence it
    will be especially useful in rare variant analysis.
	"""
	
	cran = "jacpop" 

	version("0.6", md5="e7193a66190c39377b7a10b7cbb36240")

