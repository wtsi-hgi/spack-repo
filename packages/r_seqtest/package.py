# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSeqtest(RPackage):
	"""Sequential Triangular Test

	Sequential triangular test for the arithmetic mean in one- and two-
    samples, proportions in one- and two-samples, and the Pearson's correlation
    coefficient.
	"""
	
	cran = "seqtest" 

	version("0.1-0", md5="9f5359a86cacb7f437740a5a1daa5b26")

	depends_on("r@3.2:", type=("build", "run"))
