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

	version("1.62.0", sha256="6496bbc196f6bbf9864b4f69d6974b099e986842834f008d4ab6ee19f01b80c7")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-biobase@2.5.5:", type=("build", "run"))
	depends_on("r-marray", type=("build", "run"))
