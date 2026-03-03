# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROmicspcadata(RPackage):
	"""Supporting data for package OMICsPCA

	Supporting data for package OMICsPCA
	"""
	
	bioc = "OMICsPCAdata" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/OMICsPCAdata_1.20.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/OMICsPCAdata/OMICsPCAdata_1.20.0.tar.gz"]

	version("1.20.0", md5="ba3167fdf846cb80aea07162b88c9b73")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-multiassayexperiment", type=("build", "run"))

