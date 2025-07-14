# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMirnatap(RPackage):
	"""miRNAtap: microRNA Targets - Aggregated Predictions

	The package facilitates implementation of workflows requiring miRNA predictions, it allows to integrate ranked miRNA target predictions from multiple sources available online and aggregate them with various methods which improves quality of predictions above any of the single sources. Currently predictions are available for Homo sapiens, Mus musculus and Rattus norvegicus (the last one through homology translation).
	"""
	
	bioc = "miRNAtap"

	version("1.42.0", commit="a81e69a23ae7b72c864bac8fff2b7d98ea94a20f")
	version("1.36.0", commit="f20aa1f19a54b2efe447c88eb88233fe7411e000")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-rsqlite", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-sqldf", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
