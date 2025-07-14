# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMira(RPackage):
	"""Methylation-Based Inference of Regulatory Activity

	DNA methylation contains information about the regulatory state of the cell. MIRA aggregates genome-scale DNA methylation data into a DNA methylation profile for a given region set with shared biological annotation. Using this profile, MIRA infers and scores the collective regulatory activity for the region set. MIRA facilitates regulatory analysis in situations where classical regulatory assays would be difficult and allows public sources of region sets to be leveraged for novel insight into the regulatory state of DNA methylation datasets.
	"""
	
	homepage = "http://databio.org/mira"
	bioc = "MIRA"

	version("1.30.0", commit="12fa618919952ff264bfc362b4287855751c3949")
	version("1.24.0", commit="a6d3f7cdc3e9bd6668b622c74538e300eb62203d")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-bsseq", type=("build", "run"))
