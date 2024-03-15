# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBiobase(RPackage):
	"""Biobase: Base functions for Bioconductor.

	Functions that are needed by many other packages or which replace R
	functions."""

	bioc = "Biobase"
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Biobase_2.62.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/Biobase/Biobase_2.62.0.tar.gz"]

	version("2.62.0", md5="75a65eb015d58ca611f2bebca41f9d2d")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-biocgenerics@0.27.1:", type=("build", "run"))
