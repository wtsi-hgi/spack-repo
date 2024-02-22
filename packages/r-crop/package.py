# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCrop(RPackage):
	"""Graphics Cropping Tool

	A device closing function which is able to crop graphics (e.g.,
  PDF, PNG files) on Unix-like operating systems with the required underlying
  command-line tools installed.
	"""
	
	cran = "crop" 

	version("0.0-2", md5="96b60dc98345fdb7b12ec8b8b612dd0f")

	depends_on("r@3:", type=("build", "run"))
