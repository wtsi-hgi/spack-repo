# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RReadmet(RPackage):
	"""Read some less Popular Formats Used in Meteorology

	Contains tools for reading and writing data from or to files in the formats: akterm, dmna, Scintec Format-1, and Campbell Scientific TOA5.
	"""
	
	cran = "readmet" 

	version("1.7.1", md5="95cfc52a0ba771fd96912a1f0925accd")
	version("1.6.9", md5="84f42006fce43f1d58c7275f0dc78241")

