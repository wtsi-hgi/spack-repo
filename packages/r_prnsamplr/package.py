# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPrnsamplr(RPackage):
	"""Permanent Random Number Sampling

	Survey sampling using permanent random numbers (PRN's). A solution to the
    problem of unknown overlap between survey samples, which leads to a low
    precision in estimates when the survey is repeated or combined with other
    surveys. The PRN solution is to supply the U(0, 1) random numbers to the 
    sampling procedure, instead of having the sampling procedure generate them.
    In Lindblom (2014) <doi:10.2478/jos-2014-0047>, and therein cited articles,
    it is shown how this is carried out and how it improves the estimates. This
    package supports two common fixed-size sampling procedures (simple random 
    sampling and probability-proportional-to-size sampling) and includes a 
    function for transforming the PRN's in order to control the sample overlap.
	"""
	
	cran = "prnsamplr" 

	version("0.3.0", md5="df05316c9a40e4a2851901b61723475d")

	depends_on("r@2.10:", type=("build", "run"))
