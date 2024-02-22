# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RItan(RPackage):
	"""Item Analysis for Multiple Choice Tests

	Functions for analyzing multiple choice items. These analyses include
  the convertion of student response into binaty data (correct/incorrect),
  the computation of the number of corrected responses and grade for each subject,
  the calculation of item difficulty and discrimination, the computation of the
  frecuency and point-biserial correlation for each distractor and the graphical
  analysis of each item.
	"""
	
	homepage = "https://github.com/arielarmijo/itan"
	cran = "itan" 

	version("3.1.1", md5="f87394cc0d3381377308b98dd9170d4f")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-reshape", type=("build", "run"))
