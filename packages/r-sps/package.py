# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSps(RPackage):
	"""Sequential Poisson Sampling

	Sequential Poisson sampling is a variation of Poisson sampling for
    drawing probability-proportional-to-size samples with a given number of
    units, and is commonly used for price-index surveys. This package gives
    functions to draw stratified sequential Poisson samples according to the
    method by Ohlsson (1998, ISSN:0282-423X), as well as other order sample
    designs by Rosén (1997, <doi:10.1016/S0378-3758(96)00186-3>), and generate
    appropriate bootstrap replicate weights according to the generalized
    bootstrap method by Beaumont and Patak
    (2012, <doi:10.1111/j.1751-5823.2011.00166.x>).
	"""
	
	homepage = "https://marberts.github.io/sps/"
	cran = "sps" 

	version("0.5.4", md5="84eb4bc2c3b7ad1793246c0bb2abb7b9")
	version("0.5.3", md5="004f58bcdd63098c9caa74da48590101")

	depends_on("r@4:", type=("build", "run"))
