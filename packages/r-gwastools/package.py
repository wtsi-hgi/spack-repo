# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGwastools(RPackage):
	"""Tools for Genome Wide Association Studies

	Classes for storing very large GWAS data sets and annotation, and functions for GWAS data cleaning and analysis.
	"""
	
	homepage = "https://github.com/smgogarten/GWASTools"
	bioc = "GWASTools" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/GWASTools_1.48.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/GWASTools/GWASTools_1.48.0.tar.gz"]

	version("1.54.0", tag="RELEASE_3_21")
	version("1.48.0", sha256="e8325dbba51b721e946e733bedd600136f0bc4f9aad5e45b79b5fe62386b4fe6")

	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-gdsfmt", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-rsqlite", type=("build", "run"))
	depends_on("r-gwasexacthw", type=("build", "run"))
	depends_on("r-dnacopy", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-sandwich", type=("build", "run"))
	depends_on("r-lmtest", type=("build", "run"))
	depends_on("r-logistf", type=("build", "run"))
	depends_on("r-quantsmooth", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
