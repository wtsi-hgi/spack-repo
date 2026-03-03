# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRmallow(RPackage):
	"""Fit Multi-Modal Mallows' Models to Ranking Data

	An EM algorithm to fit Mallows' Models to full or partial rankings, with or without ties.
        Based on Adkins and Flinger (1998) <doi:10.1080/03610929808832223>.
	"""
	
	cran = "RMallow" 

	version("1.1", md5="9a469dee1335f52858881cac6018f842")

	depends_on("r-combinat", type=("build", "run"))
