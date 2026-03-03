# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPps(RPackage):
	"""PPS Sampling

	Functions to select samples using PPS (probability proportional to size) sampling. The package also includes a function for stratified simple random sampling, a function to compute joint inclusion probabilities for Sampford's method of PPS sampling, and a few utility functions. The user's guide pps-ug.pdf is included in the .../pps/doc directory. The methods are described in standard survey sampling theory books such as Cochran's "Sampling Techniques"; see the user's guide for references.
	"""
	
	cran = "pps" 

	version("1.0", md5="d639aaaa13550a442ba018927b4f763a")

