# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBumphunter(RPackage):
	"""Bump Hunter.

	Tools for finding bumps in genomic data"""

	bioc = "bumphunter"
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/bumphunter_1.44.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/bumphunter/bumphunter_1.44.0.tar.gz"]

	version("1.44.0", md5="fea93f84b54daabaaf1686d658aeedfc")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-s4vectors@0.9.25:", type=("build", "run"))
	depends_on("r-iranges@2.3.23:", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-iterators", type=("build", "run"))
	depends_on("r-locfit", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-dorng", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-genomicfeatures", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
