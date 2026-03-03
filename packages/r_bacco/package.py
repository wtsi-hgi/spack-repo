# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBacco(RPackage):
	"""Bayesian Analysis of Computer Code Output (BACCO)

	The BACCO bundle of packages is replaced by the BACCO
 package, which provides a vignette that illustrates the constituent
 packages (emulator, approximator, calibrator) in use.
	"""
	
	cran = "BACCO" 

	version("2.1-0", md5="6b3a8386d0764c9bc6e9d6641a592eb8")

	depends_on("r-emulator@1.2.21:", type=("build", "run"))
	depends_on("r-calibrator@1.2.5:", type=("build", "run"))
	depends_on("r-approximator@1.2.6:", type=("build", "run"))
