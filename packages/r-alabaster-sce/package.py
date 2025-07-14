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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/alabaster.sce_1.2.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/alabaster.sce/alabaster.sce_1.2.0.tar.gz"]

	version("1.8.0", tag="RELEASE_3_21")
	version("1.2.0", sha256="7f335edf1edac01869d5d2790390af327b409acc7c5644750376cfe48e8f64be")

	depends_on("r-singlecellexperiment", type=("build", "run"))
	depends_on("r-alabaster-base", type=("build", "run"))
	depends_on("r-alabaster-se", type=("build", "run"))
