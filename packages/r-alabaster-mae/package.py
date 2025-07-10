# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAlabasterMae(RPackage):
	"""Load and Save MultiAssayExperiments

	Save MultiAssayExperiments into file artifacts, and load them back into memory. This is a more portable alternative to serialization of such objects into RDS files. Each artifact is associated with metadata for further interpretation; downstream applications can enrich this metadata with context-specific properties.
	"""
	
	bioc = "alabaster.mae" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/alabaster.mae_1.2.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/alabaster.mae/alabaster.mae_1.2.0.tar.gz"]

	version("1.2.0", sha256="319236c02b188c5e5e9b4b3828bac63f474932c25f4b1c91fbf03f738078e8a9")

	depends_on("r-multiassayexperiment", type=("build", "run"))
	depends_on("r-alabaster-base", type=("build", "run"))
	depends_on("r-alabaster-se", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
