# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNetactivitydata(RPackage):
	"""Data required for getting the gene set scores with NetActivity package

	This package contains the weights from pre-trained shallow sparsely-connected autoencoders. This data is required for getting the gene set scores with NetActivity package.
	"""
	
	bioc = "NetActivityData" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/NetActivityData_1.4.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/NetActivityData/NetActivityData_1.4.0.tar.gz"]

	version("1.10.0", tag="RELEASE_3_21")
	version("1.4.0", sha256="d4ce5ff252b9773d73edf218ab271ddeea9574d2af7957661fad5099bc8071c0")

	depends_on("r@4.2:", type=("build", "run"))

