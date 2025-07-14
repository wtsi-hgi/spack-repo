# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRepviz(RPackage):
	"""Replicate oriented Visualization of a genomic region

	RepViz enables the view of a genomic region in a simple and efficient way. RepViz allows simultaneous viewing of both intra- and intergroup variation in sequencing counts of the studied conditions, as well as their comparison to the output features (e.g. identified peaks) from user selected data analysis methods.The RepViz tool is primarily designed for chromatin data such as ChIP-seq and ATAC-seq, but can also be used with other sequencing data such as RNA-seq, or combinations of different types of genomic data.
	"""
	
	bioc = "RepViz"

	version("1.24.0", commit="79c9d6af94512aed228744e1691be4bbd2e09b91")
	version("1.18.0", commit="4732c6b5e1a6bc45fe8e55cf2c04afcf2fa78452")

	depends_on("r@3.5.1:", type=("build", "run"))
	depends_on("r-genomicranges@1.30:", type=("build", "run"))
	depends_on("r-rsamtools@1.34.1:", type=("build", "run"))
	depends_on("r-iranges@2.14:", type=("build", "run"))
	depends_on("r-biomart@2.36:", type=("build", "run"))
	depends_on("r-s4vectors@0.18:", type=("build", "run"))
