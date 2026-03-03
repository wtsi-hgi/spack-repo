# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQuiltr(RPackage):
	"""Qualtrics for Labelling Text using R

	Functions to convert text data for labelling into format appropriate for importing into Qualtrics. Supports multiple language, including right-to-left scripts as well as different response types. Outputs an Advance Format .txt file that read into Qualtrics.
	"""
	
	cran = "quiltr" 

	version("0.1.0", md5="f59bcde2bf728746226f71f4d4df8fb2")

	depends_on("r@2.10:", type=("build", "run"))
