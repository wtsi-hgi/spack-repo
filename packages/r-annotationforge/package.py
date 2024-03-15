# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAnnotationforge(RPackage):
	"""Tools for building SQLite-based annotation data packages.

	Provides code for generating Annotation packages and their databases.
	Packages produced are intended to be used with AnnotationDbi."""

	bioc = "AnnotationForge"
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/AnnotationForge_1.44.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/AnnotationForge/AnnotationForge_1.44.0.tar.gz"]

	version("1.44.0", md5="4aa011cdbdc464bbfe1542ec418e7749")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-biocgenerics@0.15.10:", type=("build", "run"))
	depends_on("r-biobase@1.17:", type=("build", "run"))
	depends_on("r-annotationdbi@1.33.14:", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-rsqlite", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
