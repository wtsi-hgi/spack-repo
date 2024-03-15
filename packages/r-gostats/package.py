# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGostats(RPackage):
	"""Tools for manipulating GO and microarrays.

	A set of tools for interacting with GO and microarray data. A variety of
	basic manipulation tools for graphs, hypothesis testing and other simple
	calculations."""

	bioc = "GOstats"
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/GOstats_2.68.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/GOstats/GOstats_2.68.0.tar.gz"]

	version("2.68.0", md5="4489bff9142d2a3357ac2de0efc1b1b4")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-biobase@1.15.29:", type=("build", "run"))
	depends_on("r-category@2.43.2:", type=("build", "run"))
	depends_on("r-graph", type=("build", "run"))
	depends_on("r-annotationdbi@0.0.89:", type=("build", "run"))
	depends_on("r-go-db@1.13:", type=("build", "run"))
	depends_on("r-rbgl", type=("build", "run"))
	depends_on("r-annotate@1.13.2:", type=("build", "run"))
	depends_on("r-annotationforge", type=("build", "run"))
	depends_on("r-rgraphviz", type=("build", "run"))
