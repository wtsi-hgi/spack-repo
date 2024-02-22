# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpyvsspy(RPackage):
	"""Spy vs. Spy Data

	Data on the Spy vs. Spy comic strip of Mad magazine, created and
   written by Antonio Prohias.
	"""
	
	homepage = "https://github.com/shabbychef/SPYvsSPY"
	cran = "SPYvsSPY" 

	version("0.1.1", md5="8571d91f21c687d92275b435847ef8a4")

	depends_on("r@2.10:", type=("build", "run"))
