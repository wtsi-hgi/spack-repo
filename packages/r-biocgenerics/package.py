# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBiocgenerics(RPackage):
	"""S4 generic functions used in Bioconductor.

	The package defines S4 generic functions used in Bioconductor."""

	bioc = "BiocGenerics"
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/BiocGenerics_0.48.1.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/BiocGenerics/BiocGenerics_0.48.1.tar.gz"]

	version("0.48.1", md5="77629e64c2a9a0324eb11bb59b53b126")

	depends_on("r@4:", type=("build", "run"))
