# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSnagee(RPackage):
	"""Signal-to-Noise applied to Gene Expression Experiments

	Signal-to-Noise applied to Gene Expression Experiments. Signal-to-noise ratios can be used as a proxy for quality of gene expression studies and samples. The SNRs can be calculated on any gene expression data set as long as gene IDs are available, no access to the raw data files is necessary. This allows to flag problematic studies and samples in any public data set.
	"""
	
	homepage = "http://bioconductor.org/"
	bioc = "SNAGEE"

	version("1.48.0", commit="ac5a58d7d88740e85ed8c9a4526b082ff4f7cb6b")
	version("1.42.0", commit="bd438eec62590d682ea20306987ae0824e4a133c")

	depends_on("r@2.6:", type=("build", "run"))
	depends_on("r-snageedata", type=("build", "run"))
