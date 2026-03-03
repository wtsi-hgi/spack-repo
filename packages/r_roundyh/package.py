# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRoundyh(RPackage):
	"""Round Dataframe

	A simple rounding function. The default round() function in R
    uses the IEC 60559 standard and therefore it rounds 0.5 to 0 and rounds
    -1.5 to -2.  The roundx() function accounts for this and helps
    to round 0.5 up to 1.
	"""
	
	cran = "roundyh" 

	version("0.1.0", md5="91929bd3ead74abab8f29cde7824adf6")

	depends_on("r@3.5:", type=("build", "run"))
