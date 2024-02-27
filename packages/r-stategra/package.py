# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStategra(RPackage):
	"""Classes and methods for multi-omics data integration

	Classes and tools for multi-omics data integration.
	"""
	
	bioc = "STATegRa" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/STATegRa_1.38.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/STATegRa/STATegRa_1.38.0.tar.gz"]

	version("1.38.0", md5="be42ca7786d4b038ad3f706492c74022")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-calibrate", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-edger", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-affy", type=("build", "run"))