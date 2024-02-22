# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAlabasterSce(RPackage):
	"""Load and Save SingleCellExperiment from File

	Save SingleCellExperiment into file artifacts, and load them back into memory. This is a more portable alternative to serialization of such objects into RDS files. Each artifact is associated with metadata for further interpretation; downstream applications can enrich this metadata with context-specific properties.
	"""
	
	bioc = "alabaster.sce" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/alabaster.sce_1.2.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/alabaster.sce/alabaster.sce_1.2.0.tar.gz"]

	version("1.2.0", md5="e508f30fb84947c7246b093b63a5aea3")

	depends_on("r-singlecellexperiment", type=("build", "run"))
	depends_on("r-alabaster-base", type=("build", "run"))
	depends_on("r-alabaster-se", type=("build", "run"))
