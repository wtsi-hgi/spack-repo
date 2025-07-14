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

	version("1.8.0", commit="d44b73b93f2be2a820d1380176786b2c87e14200")
	version("1.2.0", commit="b71e280ddc4f5f76a542c286fcb37c4f4c9ad3a2")

	depends_on("r-singlecellexperiment", type=("build", "run"))
	depends_on("r-alabaster-base", type=("build", "run"))
	depends_on("r-alabaster-se", type=("build", "run"))
