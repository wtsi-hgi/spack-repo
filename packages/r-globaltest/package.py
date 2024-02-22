# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGlobaltest(RPackage):
	"""Testing Groups of Covariates/Features for Association with a Response
	Variable, with Applications to Gene Set Testing.

	The global test tests groups of covariates (or features) for association
	with a response variable. This package implements the test with diagnostic
	plots and multiple testing utilities, along with several functions to
	facilitate the use of this test for gene set testing of GO and KEGG
	terms."""

	bioc = "globaltest"
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/globaltest_5.56.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/globaltest/globaltest_5.56.0.tar.gz"]

	version("5.56.0", md5="ca389a7105fc08bc6172ce755d842a31")

	depends_on("r-survival", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-annotate", type=("build", "run"))
