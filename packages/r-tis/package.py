# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTis(RPackage):
	"""Time Indexes and Time Indexed Series

	Functions and S3 classes for time indexes and time indexed
        series, which are compatible with FAME frequencies.
	"""
	
	cran = "tis" 

	version("1.39", md5="f06556959f1ab4767f833599c79d18b0")

	depends_on("r@2.3:", type=("build", "run"))
