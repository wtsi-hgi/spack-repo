# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGenefilter(RPackage):
	"""Methods for filtering genes from high-throughput experiments.

	Some basic functions for filtering genes."""

	bioc = "genefilter"
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/genefilter_1.84.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/genefilter/genefilter_1.84.0.tar.gz"]

	version("1.84.0", md5="15011d1662a58967aeb3e89f1f660e40")

	depends_on("r-matrixgenerics@1.11.1:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-annotate", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
