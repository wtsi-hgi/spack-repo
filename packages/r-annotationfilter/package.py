# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAnnotationfilter(RPackage):
	"""Facilities for Filtering Bioconductor Annotation Resources.

	This package provides class and other infrastructure to implement
	filters for manipulating Bioconductor annotation resources. The filters
	will be used by ensembldb, Organism.dplyr, and other packages."""

	bioc = "AnnotationFilter"
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/AnnotationFilter_1.26.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/AnnotationFilter/AnnotationFilter_1.26.0.tar.gz"]

	version("1.26.0", md5="512eececc247990236fd09aa1fc46966")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-lazyeval", type=("build", "run"))
