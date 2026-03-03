# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDate(RPackage):
	"""Functions for Handling Dates

	Functions for handling dates.
	"""
	
	cran = "date" 

	version("1.2-42", md5="6f964749607b4f7adcca5c68bcb5c7bb")

