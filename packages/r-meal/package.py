# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMeal(RPackage):
	"""Perform methylation analysis

	Package to integrate methylation and expression data. It can also perform methylation or expression analysis alone. Several plotting functionalities are included as well as a new region analysis based on redundancy analysis. Effect of SNPs on a region can also be estimated.
	"""
	
	bioc = "MEAL" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/MEAL_1.32.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/MEAL/MEAL_1.32.0.tar.gz"]

	version("1.32.0", md5="f157edf85ba036b17edb728a44e2e519")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-multidataset", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-vegan", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-minfi", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-ggplot2@2:", type=("build", "run"))
	depends_on("r-permute", type=("build", "run"))
	depends_on("r-gviz", type=("build", "run"))
	depends_on("r-missmethyl", type=("build", "run"))
	depends_on("r-isva", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-smartsva", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
