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

    version("1.36.0", tag="RELEASE_3_21")
	version("1.30.0", sha256="40b14402c428e86b209c10363425f18257afff90788bd6e0db7e1723d942c2bd")


