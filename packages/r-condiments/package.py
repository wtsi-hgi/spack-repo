# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCondiments(RPackage):
	"""Differential Topology, Progression and Differentiation

	This package encapsulate many functions to conduct a differential topology analysis. It focuses on analyzing an 'omic dataset with multiple conditions. While the package is mostly geared toward scRNASeq, it does not place any restriction on the actual input format.
	"""
	
	homepage = "https://hectorrdb.github.io/condiments/index.html"
	bioc = "condiments" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/condiments_1.10.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/condiments/condiments_1.10.0.tar.gz"]

	version("1.10.0", md5="63b9756275a532e7d38c67402cef7efd")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-slingshot@1.9:", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-rann", type=("build", "run"))
	depends_on("r-singlecellexperiment", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-ecume@0.9.1:", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-trajectoryutils", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-distinct", type=("build", "run"))
