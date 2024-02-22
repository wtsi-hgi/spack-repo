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
	urls = ["https://www.bioconductor.org/packages/release/data/experiment/src/contrib/NetActivityData_1.4.0.tar.gz", "https://www.bioconductor.org/packages/release/data/experiment/src/contrib/Archive/NetActivityData/NetActivityData_1.4.0.tar.gz"]

	version("1.4.0", md5="a3805046d14d13afc30a0f082952f200")

	depends_on("r@4.2:", type=("build", "run"))

	# experiment