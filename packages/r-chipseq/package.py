# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RChipseq(RPackage):
	"""A package for analyzing chipseq data,

	Tools for helping process short read data for chipseq experiments"""

	bioc = "chipseq"

	maintainers("dorton21")
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/chipseq_1.52.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/chipseq/chipseq_1.52.0.tar.gz"]

	version("1.52.0", md5="5cf8ab297fc95d0a36b4359488c50358")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-s4vectors@0.17.25:", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-shortread", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
