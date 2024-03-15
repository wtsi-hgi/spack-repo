# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpqndata(RPackage):
	"""Data for the spqn package

	Bulk RNA-seq from GTEx on 4,000 randomly selected, expressed genes. Data has been processed for co-expression analysis.
	"""
	
	bioc = "spqnData" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/spqnData_1.14.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/spqnData/spqnData_1.14.0.tar.gz"]

	version("1.14.0", md5="453bf944ea40956afef2bd868f92d747")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))

	# experiment