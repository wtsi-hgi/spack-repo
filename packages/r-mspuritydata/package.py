# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMspuritydata(RPackage):
	"""Fragmentation spectral libraries and data to test the msPurity package

	Fragmentation spectral libraries and data to test the msPurity package
	"""
	
	bioc = "msPurityData" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/msPurityData_1.30.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/msPurityData/msPurityData_1.30.0.tar.gz"]

	version("1.30.0", md5="6c86343515cbb9f81131baa3f25659f0")


	# experiment