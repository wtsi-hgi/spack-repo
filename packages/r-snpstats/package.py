# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSnpstats(RPackage):
	"""SnpMatrix and XSnpMatrix classes and methods.

	Classes and statistical methods for large SNP association studies. This
	extends the earlier snpMatrix package, allowing for uncertainty in
	genotypes."""

	bioc = "snpStats"
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/snpStats_1.52.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/snpStats/snpStats_1.52.0.tar.gz"]

	version("1.52.0", md5="0625c920470937a31fd278cf8bd8982a")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-zlibbioc", type=("build", "run"))
	depends_on("zlib", type=("build", "link", "run"))
