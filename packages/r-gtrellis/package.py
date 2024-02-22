# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGtrellis(RPackage):
	"""Genome Level Trellis Layout.

	Genome level Trellis graph visualizes genomic data conditioned by
	genomic categories (e.g. chromosomes). For each genomic category,
	multiple dimensional data which are represented as tracks describe
	different features from different aspects. This package provides high
	flexibility to arrange genomic categories and to add self-defined
	graphics in the plot."""

	bioc = "gtrellis"
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/gtrellis_1.34.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/gtrellis/gtrellis_1.34.0.tar.gz"]

	version("1.34.0", md5="795b74d96310e3cd9a5771bd8695cf64")

	depends_on("r@3.1.2:", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-circlize@0.4.8:", type=("build", "run"))
	depends_on("r-getoptlong", type=("build", "run"))
