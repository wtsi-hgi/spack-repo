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

	version("1.8.0", commit="70ab20b39f6e2e6b43dc8524d7a4422b86ecce53")
	version("1.2.0", commit="4636dc2f21528cde282348805a8a510dc3bd3521")

	depends_on("r-multiassayexperiment", type=("build", "run"))
	depends_on("r-alabaster-base", type=("build", "run"))
	depends_on("r-alabaster-se", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
