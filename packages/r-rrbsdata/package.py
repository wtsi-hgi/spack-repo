# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRrbsdata(RPackage):
	"""An RRBS data set with 12 samples and 10,000 simulated DMRs

	RRBS data set comprising 12 samples with simulated differentially methylated regions (DMRs).
	"""
	
	bioc = "RRBSdata"

	version("1.28.0", commit="77bb5d5ab044d39395646b5a1ecb1b7f530539c4")
	version("1.22.0", commit="43693cd9d8c2b8a08adccb06927939b3d4ae88ac")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-biseq@1.9.2:", type=("build", "run"))

