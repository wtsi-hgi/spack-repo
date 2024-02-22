# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RXicor(RPackage):
	"""Association Measurement Through Cross Rank Increments

	Computes robust association measures that do not 
    presuppose linearity. The xi correlation (xicor) is based
    on cross correlation between ranked increments.
    The reference for the methods implemented here is 
    Chatterjee, Sourav (2020) <arXiv:1909.10140>
    This package includes the Galton peas example.
	"""
	
	cran = "XICOR" 

	version("0.4.1", md5="db8d62d2441c23e111f16a938992f2c5")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-psychtools", type=("build", "run"))
