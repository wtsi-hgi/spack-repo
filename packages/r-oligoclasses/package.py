# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROligoclasses(RPackage):
	"""Classes for high-throughput arrays supported by oligo and crlmm.

	This package contains class definitions, validity checks, and
	initialization methods for classes used by the oligo and crlmm
	packages."""

	bioc = "oligoClasses"
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/oligoClasses_1.64.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/oligoClasses/oligoClasses_1.64.0.tar.gz"]

	version("1.64.0", md5="379f1364d7159e2456c9310556e990e6")

	depends_on("r@2.14:", type=("build", "run"))
	depends_on("r-biocgenerics@0.27.1:", type=("build", "run"))
	depends_on("r-biobase@2.17.8:", type=("build", "run"))
	depends_on("r-iranges@2.5.17:", type=("build", "run"))
	depends_on("r-genomicranges@1.23.7:", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-biostrings@2.23.6:", type=("build", "run"))
	depends_on("r-affyio@1.23.2:", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-biocmanager", type=("build", "run"))
	depends_on("r-s4vectors@0.9.25:", type=("build", "run"))
	depends_on("r-rsqlite", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-ff", type=("build", "run"))
