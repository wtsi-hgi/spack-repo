# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAffy(RPackage):
	"""Methods for Affymetrix Oligonucleotide Arrays.

	The package contains functions for exploratory oligonucleotide array
	analysis. The dependence on tkWidgets only concerns few convenience
	functions. 'affy' is fully functional without it."""

	bioc = "affy"
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/affy_1.80.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/affy/affy_1.80.0.tar.gz"]

	version("1.80.0", md5="09376016b32f86f707ff9b8f8cb8a1a5")

	depends_on("r@2.8:", type=("build", "run"))
	depends_on("r-biocgenerics@0.1.12:", type=("build", "run"))
	depends_on("r-biobase@2.5.5:", type=("build", "run"))
	depends_on("r-affyio@1.13.3:", type=("build", "run"))
	depends_on("r-biocmanager", type=("build", "run"))
	depends_on("r-preprocesscore", type=("build", "run"))
	depends_on("r-zlibbioc", type=("build", "run"))
