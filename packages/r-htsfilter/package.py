# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHtsfilter(RPackage):
	"""Filter replicated high-throughput transcriptome sequencing data

	This package implements a filtering procedure for replicated transcriptome sequencing data based on a global Jaccard similarity index in order to identify genes with low, constant levels of expression across one or more experimental conditions.
	"""
	
	bioc = "HTSFilter"

	version("1.48.0", commit="9bcd7006d6b269a158510ac613c3da8a2c7a954b")
	version("1.42.0", commit="ca57c533f877adcf4e3fb94341cdb1dc28ff6c14")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-edger", type=("build", "run"))
	depends_on("r-deseq2", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
