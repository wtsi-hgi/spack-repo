# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBladderbatch(RPackage):
	"""Bladder gene expression data illustrating batch effects

	This package contains microarray gene expression data on 57 bladder samples from 5 batches. The data are used as an illustrative example for the sva package.
	"""
	
	bioc = "bladderbatch" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/bladderbatch_1.40.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/bladderbatch/bladderbatch_1.40.0.tar.gz"]

	version("1.40.0", md5="d59d10a87e8d62c6ba10f7e9c0160a44")

	depends_on("r-biobase", type=("build", "run"))

