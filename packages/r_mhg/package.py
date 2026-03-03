# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMhg(RPackage):
	"""Minimum-Hypergeometric Test

	Runs a minimum-hypergeometric (mHG) test as described in: Eden, E. (2007). Discovering Motifs in Ranked Lists of DNA Sequences. Haifa. 
	"""
	
	cran = "mHG" 

	version("1.1", md5="79f276a07210641fbc43326cbf3b9e62")

