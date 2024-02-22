# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RA4(RPackage):
	"""Automated Affymetrix Array Analysis Umbrella Package.

	Umbrella package is available for the entire Automated Affymetrix Array
	Analysis suite of package."""

	bioc = "a4"
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/a4_1.50.1.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/a4/a4_1.50.1.tar.gz"]

	version("1.50.1", md5="deef7e8b7ef01abfdd310cc5d5ba9225", url="https://www.bioconductor.org/packages/release/bioc/src/contrib/a4_1.50.1.tar.gz")

	depends_on("r-a4base", type=("build", "run"))
	depends_on("r-a4preproc", type=("build", "run"))
	depends_on("r-a4classif", type=("build", "run"))
	depends_on("r-a4core", type=("build", "run"))
	depends_on("r-a4reporting", type=("build", "run"))
