# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGcrma(RPackage):
	"""Background Adjustment Using Sequence Information.

	Background adjustment using sequence information."""

	bioc = "gcrma"
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/gcrma_2.74.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/gcrma/gcrma_2.74.0.tar.gz"]

	version("2.74.0", md5="d28b6c225b2677e476da8d0348af4695")

	depends_on("r@2.6:", type=("build", "run"))
	depends_on("r-affy@1.23.2:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-affyio@1.13.3:", type=("build", "run"))
	depends_on("r-xvector", type=("build", "run"))
	depends_on("r-biostrings@2.11.32:", type=("build", "run"))
	depends_on("r-biocmanager", type=("build", "run"))
