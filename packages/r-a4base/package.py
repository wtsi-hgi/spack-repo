# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RA4base(RPackage):
	"""Automated Affymetrix Array Analysis Base Package.

	Base utility functions are available for the Automated Affymetrix Array
	Analysis set of packages."""

	bioc = "a4Base"
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/a4Base_1.50.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/a4Base/a4Base_1.50.0.tar.gz"]

	version("1.50.0", md5="927ee5147653a1ee4df6380f52ad055a")

	depends_on("r-a4preproc", type=("build", "run"))
	depends_on("r-a4core", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-annaffy", type=("build", "run"))
	depends_on("r-mpm", type=("build", "run"))
	depends_on("r-genefilter", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-multtest", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
