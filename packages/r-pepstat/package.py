# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPepstat(RPackage):
	"""Statistical analysis of peptide microarrays

	Statistical analysis of peptide microarrays
	"""
	
	homepage = "https://github.com/RGLab/pepStat"
	bioc = "pepStat" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/pepStat_1.36.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/pepStat/pepStat_1.36.0.tar.gz"]

	version("1.36.0", md5="031af81c6bcac97b7262d978bfda2392")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-fields", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
