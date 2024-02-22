# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RImpute(RPackage):
	"""impute: Imputation for microarray data.

	Imputation for microarray data (currently KNN only)"""

	bioc = "impute"
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/impute_1.76.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/impute/impute_1.76.0.tar.gz"]

	version("1.76.0", md5="8e974dcc31c3507ebcc8984b2d7943f9")

	depends_on("r@2.10:", type=("build", "run"))
