# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAffyplm(RPackage):
	"""Methods for fitting probe-level models.

	A package that extends and improves the functionality of the base affy
	package. Routines that make heavy use of compiled code for speed.
	Central focus is on implementation of methods for fitting probe-level
	models and tools using these models. PLM based quality assessment
	tools."""

	bioc = "affyPLM"
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/affyPLM_1.78.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/affyPLM/affyPLM_1.78.0.tar.gz"]

	version("1.78.0", md5="cdfd69bc9c54f3c03b52b3fd6e9f86b7")

	depends_on("r@2.6:", type=("build", "run"))
	depends_on("r-biocgenerics@0.3.2:", type=("build", "run"))
	depends_on("r-affy@1.11:", type=("build", "run"))
	depends_on("r-biobase@2.17.8:", type=("build", "run"))
	depends_on("r-gcrma", type=("build", "run"))
	depends_on("r-preprocesscore", type=("build", "run"))
	depends_on("r-zlibbioc", type=("build", "run"))
