# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIcr(RPackage):
	"""Compute Krippendorff's Alpha

	Provides functions to compute and plot Krippendorff's inter-coder 
    reliability coefficient alpha and bootstrapped uncertainty estimates 
    (Krippendorff 2004, ISBN:0761915443). The bootstrap routines are set up to
    make use of parallel threads where supported.
	"""
	
	homepage = "https://github.com/staudtlex/icr"
	cran = "icr" 

	version("0.6.5", md5="cb32f85e3bf9a1dd8a9c84632ecda305")
	version("0.6.4", md5="8083925bb60e239d4266f7813cc22958")

	depends_on("r-rcpp", type=("build", "run"))
