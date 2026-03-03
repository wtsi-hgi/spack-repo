# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSynapterdata(RPackage):
	"""Data accompanying the synapter package

	Data independant acquisition of UPS1 protein mix in an E. coli background obtained on a Waters Synapt G2 instrument.
	"""
	
	bioc = "synapterdata" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/synapterdata_1.40.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/synapterdata/synapterdata_1.40.0.tar.gz"]

	version("1.40.0", md5="255aa756f0b6c0c1d95cdfbc889a67a2")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-synapter@1.99.2:", type=("build", "run"))

