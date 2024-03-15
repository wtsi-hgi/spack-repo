# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCghbase(RPackage):
	"""CGHbase: Base functions and classes for arrayCGH data analysis.

	Contains functions and classes that are needed by arrayCGH packages.
	"""
	
	homepage = "https://github.com/tgac-vumc/CGHbase"
	bioc = "CGHbase" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/CGHbase_1.62.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/CGHbase/CGHbase_1.62.0.tar.gz"]

	version("1.62.0", md5="806f73dc042c0bf46989606a4aa4dbe8")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-biobase@2.5.5:", type=("build", "run"))
	depends_on("r-marray", type=("build", "run"))
