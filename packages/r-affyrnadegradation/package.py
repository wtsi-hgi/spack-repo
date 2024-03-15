# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAffyrnadegradation(RPackage):
	"""Analyze and correct probe positional bias in microarray data due to RNA
	degradation.

	The package helps with the assessment and correction of RNA degradation
	effects in Affymetrix 3' expression arrays. The parameter d gives a
	robust and accurate measure of RNA integrity. The correction removes the
	probe positional bias, and thus improves comparability of samples that
	are affected by RNA degradation."""

	bioc = "AffyRNADegradation"
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/AffyRNADegradation_1.48.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/AffyRNADegradation/AffyRNADegradation_1.48.0.tar.gz"]

	version("1.48.0", md5="4affd7f48b178750311671c1f2ac8c4f")

	depends_on("r@2.9:", type=("build", "run"))
	depends_on("r-affy", type=("build", "run"))
