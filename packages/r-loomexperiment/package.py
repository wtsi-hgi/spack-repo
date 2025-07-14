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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/LoomExperiment_1.20.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/LoomExperiment/LoomExperiment_1.20.0.tar.gz"]

	version("1.26.1", tag="RELEASE_3_21")
	version("1.20.0", sha256="f3504f85c21760ff83f76c51a5170493add240fd777cd9a4199c165d822b8c57")

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
