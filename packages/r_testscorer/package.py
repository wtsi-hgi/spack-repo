# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTestscorer(RPackage):
	"""GUI for Entering Test Items and Obtaining Raw and Transformed
Scores

	GUI for entering test items and obtaining raw
   and transformed scores. The results are shown on the
   console and can be saved to a tabular text file for further
   statistical analysis. The user can define his own tests and
   scoring procedures through a GUI.
	"""
	
	cran = "TestScorer" 

	version("1.7.2", md5="79385b608c25b448055897116eed9334")

