# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMacsquantifyr(RPackage):
	"""Fast treatment of MACSQuantify FACS data

	Automatically process the metadata of MACSQuantify FACS sorter. It runs multiple modules: i) imports of raw file and graphical selection of duplicates in well plate, ii) computes statistics on data and iii) can compute combination index.
	"""
	
	bioc = "MACSQuantifyR" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/MACSQuantifyR_1.16.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/MACSQuantifyR/MACSQuantifyR_1.16.0.tar.gz"]

	version("1.22.0", tag="RELEASE_3_21")
	version("1.16.0", sha256="a1e9a9c20333d22f719a0d7bf6da85a8a07282ece3b87f295fc9756ac0943d79")

	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-latticeextra", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-png", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-prettydoc", type=("build", "run"))
	depends_on("r-rvest", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
