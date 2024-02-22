# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAcme(RPackage):
	"""Algorithms for Calculating Microarray Enrichment (ACME).

	ACME (Algorithms for Calculating Microarray Enrichment) is a set of
	tools for analysing tiling array ChIP/chip, DNAse hypersensitivity, or
	other experiments that result in regions of the genome showing
	"enrichment". It does not rely on a specific array technology (although
	the array should be a "tiling" array), is very general (can be applied
	in experiments resulting in regions of enrichment), and is very
	insensitive to array noise or normalization methods. It is also very
	fast and can be applied on whole-genome tiling array experiments quite
	easily with enough memory."""

	bioc = "ACME"
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/ACME_2.58.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/ACME/ACME_2.58.0.tar.gz"]

	version("2.58.0", md5="6668a82e0a26ac03c9697e2cf22eb75e")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-biobase@2.5.5:", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
