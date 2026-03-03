# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSwdft(RPackage):
	"""Sliding Window Discrete Fourier Transform (SWDFT)

	Implements the Sliding Window Discrete Fourier Transform (SWDFT). Also provides 
             statistical methods based on the SWDFT, and graphical tools to display the outputs.
	"""
	
	cran = "swdft" 

	version("1.0.0", md5="8baf9b33f7aa3ed5c39dbfbdcfb28c50")

	depends_on("r@3.3:", type=("build", "run"))
