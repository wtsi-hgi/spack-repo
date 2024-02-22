# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMleTools(RPackage):
	"""Expected/Observed Fisher Information and Bias-Corrected Maximum
Likelihood Estimate(s)

	Calculates the expected/observed Fisher information and the bias-corrected maximum likelihood estimate(s) via Cox-Snell Methodology.
	"""
	
	cran = "mle.tools" 

	version("1.0.0", md5="ea907b283c4a37a3734f04e389780b32")

	depends_on("r@3.0.2:", type=("build", "run"))
