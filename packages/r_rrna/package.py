# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRrna(RPackage):
	"""Secondary Structure Plotting for RNA

	Functions for creating and manipulating RNA secondary structure plots.
	"""
	
	cran = "RRNA" 

	version("1.0", md5="233a585baedb5925b88a9df5f3809913")

