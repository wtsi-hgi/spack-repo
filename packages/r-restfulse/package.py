# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRestfulse(RPackage):
	"""Access matrix-like HDF5 server content or BigQuery content through a SummarizedExperiment interface

	This package provides functions and classes to interface with remote data stores by operating on SummarizedExperiment-like objects.
	"""
	
	bioc = "restfulSE"

	version("1.24.0", commit="815453885cdb77eeb880eca99f6a656144f7a917")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-delayedarray", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-go-db", type=("build", "run"))
	depends_on("r-rhdf5client", type=("build", "run"))
	depends_on("r-dplyr@0.7.1:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-bigrquery", type=("build", "run"))
	depends_on("r-experimenthub", type=("build", "run"))
	depends_on("r-annotationhub", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
