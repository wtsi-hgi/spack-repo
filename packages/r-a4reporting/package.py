# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RA4reporting(RPackage):
	"""Automated Affymetrix Array Analysis Reporting Package.

	Utility functions to facilitate the reporting of the Automated Affymetrix
	Array Analysis Reporting set of packages."""

	bioc = "a4Reporting"
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/a4Reporting_1.50.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/a4Reporting/a4Reporting_1.50.0.tar.gz"]

	version("1.50.0", md5="3ba7f3c5606c2f898d84314ba63208fa")

	depends_on("r-xtable", type=("build", "run"))
