# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGenemeta(RPackage):
	"""MetaAnalysis for High Throughput Experiments.

	A collection of meta-analysis tools for analysing high throughput
	experimental data"""

	bioc = "GeneMeta"
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/GeneMeta_1.74.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/GeneMeta/GeneMeta_1.74.0.tar.gz"]

	version("1.74.0", md5="9d9d2d3dff0ee8a497ac86b5ef8ddac7")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-biobase@2.5.5:", type=("build", "run"))
	depends_on("r-genefilter", type=("build", "run"))
