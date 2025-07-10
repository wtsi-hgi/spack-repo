# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpikeinsubset(RPackage):
	"""Part of Affymetrix's Spike-In Experiment Data

	Includes probe-level and expression data for the HGU133 and HGU95 spike-in experiments
	"""
	
	homepage = "https://bioconductor.org/packages/SpikeInSubset"
	bioc = "SpikeInSubset" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/SpikeInSubset_1.42.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/SpikeInSubset/SpikeInSubset_1.42.0.tar.gz"]

	version("1.42.0", sha256="397e37d064cefe90e3869c79cb1cd6c243b07a96e26217797a35580bac798493")

	depends_on("r@2.4:", type=("build", "run"))
	depends_on("r-biobase@2.5.5:", type=("build", "run"))
	depends_on("r-affy@1.23.4:", type=("build", "run"))

