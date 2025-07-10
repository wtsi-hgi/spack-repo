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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/STATegRa_1.38.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/STATegRa/STATegRa_1.38.0.tar.gz"]

	version("1.38.0", sha256="b3051c59994ed4fbeb47d030adcc56124c892d49c12c3d74164b7d67f032505c")

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
