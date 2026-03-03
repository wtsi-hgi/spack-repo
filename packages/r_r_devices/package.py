# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRDevices(RPackage):
	"""Unified Handling of Graphics Devices

	Functions for creating plots and image files in a unified way
    regardless of output format (EPS, PDF, PNG, SVG, TIFF, WMF, etc.). Default
    device options as well as scales and aspect ratios are controlled in a uniform
    way across all device types. Switching output format requires minimal changes
    in code. This package is ideal for large-scale batch processing, because it
    will never leave open graphics devices or incomplete image files behind, even on
    errors or user interrupts.
	"""
	
	homepage = "https://henrikbengtsson.github.io/R.devices/"
	cran = "R.devices" 

	version("2.17.2", md5="54cbe1c20abe0d1db6a32ac3294a7687")

	depends_on("r@2.14:", type=("build", "run"))
	depends_on("r-r-methodss3@1.8.1:", type=("build", "run"))
	depends_on("r-r-oo@1.24:", type=("build", "run"))
	depends_on("r-r-utils@2.10.1:", type=("build", "run"))
	depends_on("r-base64enc@0.1.2:", type=("build", "run"))
