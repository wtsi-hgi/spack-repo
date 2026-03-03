# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCnprep(RPackage):
	"""Pre-Process DNA Copy Number (CN) Data for Detection of CN Events

	DNA copy number data evaluation using both their initial form 
    (copy number as a noisy function of genomic position) and their 
    approximation by a piecewise-constant function (segmentation), 
    for the purpose of identifying genomic regions where the copy number 
    differs from the norm.
	"""
	
	cran = "CNprep" 

	version("2.2", md5="4b6ddc37df607c79b7fb50a96a57197f")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-mclust", type=("build", "run"))
	depends_on("r-rlecuyer", type=("build", "run"))
