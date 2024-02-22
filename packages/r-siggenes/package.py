# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSiggenes(RPackage):
	"""Multiple Testing using SAM and Efron's Empirical Bayes Approaches.

	Identification of differentially expressed genes and estimation of the
	False Discovery Rate (FDR) using both the Significance Analysis of
	Microarrays (SAM) and the Empirical Bayes Analyses of Microarrays
	(EBAM)."""

	bioc = "siggenes"
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/siggenes_1.76.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/siggenes/siggenes_1.76.0.tar.gz"]

	version("1.76.0", md5="ae9899f2a3587a423169a27502868709")

	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-multtest", type=("build", "run"))
	depends_on("r-scrime@1.2.5:", type=("build", "run"))
