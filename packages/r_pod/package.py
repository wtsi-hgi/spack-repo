# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPod(RPackage):
	"""Probability of Detection for Qualitative PCR Methods

	This tool computes the probability of detection (POD) curve and the limit of detection (LOD), i.e. the number of copies of the target DNA sequence required to ensure a 95 % probability of detection (LOD95). Other quantiles of the LOD can be specified.
    This is a reimplementation of the mathematical-statistical modelling of the validation of qualitative polymerase chain reaction (PCR) methods within a single laboratory as provided by the commercial tool 'PROLab' <http://quodata.de/>. The modelling itself has been described by Uhlig et al. (2015) <doi:10.1007/s00769-015-1112-9>.
	"""
	
	cran = "POD" 

	version("1.2.0", md5="bfda9e2ace33dfa219a55a1df23fbc25")

	depends_on("r@3.4:", type=("build", "run"))
