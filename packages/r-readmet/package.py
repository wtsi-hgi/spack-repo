# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RReadmet(RPackage):
	"""Read some less Popular Formats Used in Meteorology

	Contains tools for reading and writing data from or to files in dmna, Scintec Format-1, and Campbell Scientific TOA5 formats.
	"""
	
	cran = "readmet" 

	version("1.6.9", md5="84f42006fce43f1d58c7275f0dc78241")

