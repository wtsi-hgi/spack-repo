# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBinfunest(RPackage):
	"""Estimates Parameters of Functions Driving Binomial Random
Variables

	Provides maximum likelihood estimates of the 
    performance parameters that drive a binomial distribution of observed 
    errors, and takes full advantage of zero error observations. High performance 
    communications systems typically have inherent noise sources and other 
    performance limitations that need to be estimated. Measurements made at 
    high signal to noise ratios typically result in zero 
    errors due to limitation in available measurement time. Package includes 
    theoretical performance functions for common modulation schemes (Proakis, 
    "Digital Communications" (1995, <ISBN:0-07-051726-6>)), polarization shifted 
    QPSK (Agrell & Karlsson (2009, <DOI:10.1109/JLT.2009.2029064>)), and utility 
    functions to work with the performance functions.
	"""
	
	homepage = "https://github.com/PhilShea/binfunest"
	cran = "binfunest" 

	version("0.1.0", md5="d7924fa76740d7f769ebd51d797e600b")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
