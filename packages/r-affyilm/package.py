# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAffyilm(RPackage):
	"""Linear Model of background subtraction and the Langmuir isotherm.

	affyILM is a preprocessing tool which estimates gene expression levels
	for Affymetrix Gene Chips. Input from physical chemistry is employed to
	first background subtract intensities before calculating concentrations
	on behalf of the Langmuir model."""

	bioc = "affyILM"
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/affyILM_1.54.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/affyILM/affyILM_1.54.0.tar.gz"]

	version("1.54.0", md5="96d1989fb75742f6a9b0f9d8df1c3fc0")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-gcrma", type=("build", "run"))
	depends_on("r-affxparser@1.16:", type=("build", "run"))
	depends_on("r-affy", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
