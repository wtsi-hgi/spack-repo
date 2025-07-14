# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLoomexperiment(RPackage):
	"""LoomExperiment container

	The LoomExperiment package provide a means to easily convert the Bioconductor "Experiment" classes to loom files and vice versa.
	"""
	
	bioc = "LoomExperiment"

	version("1.26.1", commit="f276ae5ceee6f920a7691545444c64771f4690cd")
	version("1.20.0", commit="92027674d01f74c0f5ab0b6357ca2c02c2183503")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-singlecellexperiment", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-rhdf5", type=("build", "run"))
	depends_on("r-biocio", type=("build", "run"))
	depends_on("r-delayedarray", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-hdf5array", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
