# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTinysnapshot(RPackage):
	"""Snapshots for Unit Tests using the 'tinytest' Framework

	Snapshots for unit tests using the 'tinytest' framework for R. Includes expectations to test base R and 'ggplot2' plots as well as console output from print().
	"""
	
	homepage = "https://github.com/vincentarelbundock/tinysnapshot"
	cran = "tinysnapshot" 

	version("0.0.4", md5="602170ab19559180f2b062b43b94f48c")

	depends_on("r-diffobj", type=("build", "run"))
	depends_on("r-magick@2.7.4:", type=("build", "run"))
	depends_on("r-tinytest@1.4.1:", type=("build", "run"))
