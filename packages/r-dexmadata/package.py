# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDexmadata(RPackage):
	"""Data package for DExMA package

	Data objects needed to allSameID() function of DExMA package. There are also some objects that are necessary to be able to apply the examples of the DExMA package, which illustrate package functionality.
	"""
	
	bioc = "DExMAdata" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/DExMAdata_1.10.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/DExMAdata/DExMAdata_1.10.0.tar.gz"]

	version("1.10.0", md5="3d2a9cc7d0044ffc23e572f4c5cc4426")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))

	# experiment