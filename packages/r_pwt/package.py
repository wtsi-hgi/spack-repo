# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPwt(RPackage):
	"""Penn World Table (Versions 5.6, 6.x, 7.x)

	The Penn World Table provides purchasing power parity and
	national income accounts converted to international prices for
	189 countries for some or all of the years 1950-2010.
	"""
	
	cran = "pwt" 

	version("7.1-1", md5="06c3845e8c0c2cb0fd2b9ff17f34273b")

	depends_on("r@2.10:", type=("build", "run"))
