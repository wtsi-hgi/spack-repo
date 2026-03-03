# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBucss(RPackage):
	"""Bias and Uncertainty Corrected Sample Size

	Bias- and Uncertainty-Corrected Sample Size. BUCSS implements a method of correcting for publication bias and
    uncertainty when planning sample sizes in a future study from an original study. See Anderson, Kelley, & Maxwell (2017; Psychological Science, 28, 1547-1562). 
	"""
	
	cran = "BUCSS" 

	version("1.2.1", md5="e841ce9b615051e36bf8f9cc283709f5")

