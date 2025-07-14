# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCategorycompare(RPackage):
	"""Meta-analysis of high-throughput experiments using feature annotations

	Calculates significant annotations (categories) in each of two (or more) feature (i.e. gene) lists, determines the overlap between the annotations, and returns graphical and tabular data about the significant annotations and which combinations of feature lists the annotations were found to be significant. Interactive exploration is facilitated through the use of RCytoscape (heavily suggested).
	"""
	
	homepage = "https://github.com/rmflight/categoryCompare"
	bioc = "categoryCompare" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/categoryCompare_1.46.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/categoryCompare/categoryCompare_1.46.0.tar.gz"]

	version("1.52.0", tag="RELEASE_3_21")
	version("1.46.0", sha256="043df1a80bfce24b3a62b0dc2f01509c8801f8c60751b0337adc118e2750aa0d")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-biocgenerics@0.13.8:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-hwriter", type=("build", "run"))
	depends_on("r-gseabase", type=("build", "run"))
	depends_on("r-category@2.33.1:", type=("build", "run"))
	depends_on("r-gostats", type=("build", "run"))
	depends_on("r-annotate", type=("build", "run"))
	depends_on("r-colorspace", type=("build", "run"))
	depends_on("r-graph", type=("build", "run"))
	depends_on("r-rcy3@1.99.29:", type=("build", "run"))
