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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/pepStat_1.36.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/pepStat/pepStat_1.36.0.tar.gz"]

	version("1.36.0", sha256="74447adfd8a1ce88b756445c97de9c17cb24b4ff1d8dcef48bf5836b25ffa165")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-fields", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
