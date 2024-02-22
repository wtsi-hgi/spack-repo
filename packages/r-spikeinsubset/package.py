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
	urls = ["https://www.bioconductor.org/packages/release/data/experiment/src/contrib/SpikeInSubset_1.42.0.tar.gz", "https://www.bioconductor.org/packages/release/data/experiment/src/contrib/Archive/SpikeInSubset/SpikeInSubset_1.42.0.tar.gz"]

	version("1.42.0", md5="0c9b5af679c89a1468c9a6f581202e2b")

	depends_on("r@2.4:", type=("build", "run"))
	depends_on("r-biobase@2.5.5:", type=("build", "run"))
	depends_on("r-affy@1.23.4:", type=("build", "run"))

	# experiment