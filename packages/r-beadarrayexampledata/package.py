# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBeadarrayexampledata(RPackage):
	"""Example data for the beadarray package

	An small dataset that can be used to run examples from the beadarray vignette and examples
	"""
	
	bioc = "beadarrayExampleData" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/beadarrayExampleData_1.40.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/beadarrayExampleData/beadarrayExampleData_1.40.0.tar.gz"]

	version("1.40.0", md5="d327e659adc868f1e3c7ae457c60087b")

	depends_on("r@2.13:", type=("build", "run"))
	depends_on("r-biobase@2.5.5:", type=("build", "run"))
	depends_on("r-beadarray@2:", type=("build", "run"))

	# experiment