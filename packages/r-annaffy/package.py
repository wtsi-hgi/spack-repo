# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAnnaffy(RPackage):
	"""Annotation tools for Affymetrix biological metadata.

	Functions for handling data from Bioconductor Affymetrix annotation data
	packages. Produces compact HTML and text reports including experimental
	data and URL links to many online databases. Allows searching biological
	metadata using various criteria."""

	bioc = "annaffy"
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/annaffy_1.74.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/annaffy/annaffy_1.74.0.tar.gz"]

	version("1.74.0", md5="a590578d3e87dbab236a5531f0a5bce0")

	depends_on("r@2.5:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-biocmanager", type=("build", "run"))
	depends_on("r-go-db", type=("build", "run"))
	depends_on("r-annotationdbi@0.1.15:", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
