# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSsrmLogmer(RPackage):
	"""Sample Size Determination for Longitudinal Designs with Binary
Outcome

	Provides the necessary sample size for a longitudinal study with binary outcome in order to attain a pre-specified power while strictly maintaining the Type I error rate. 
 Kapur K, Bhaumik R, Tang XC, Hur K, Reda DJ, Bhaumik D (2014) <doi:10.1002/sim.6203>.
	"""
	
	cran = "ssrm.logmer" 

	version("0.1", md5="f6aac0a78faca196a43bc865839775f4")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-statmod", type=("build", "run"))
	depends_on("r-sfsmisc", type=("build", "run"))
