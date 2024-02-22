# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScatterhatch(RPackage):
	"""Creates hatched patterns for scatterplots

	The objective of this package is to efficiently create scatterplots where groups can be distinguished by color and texture. Visualizations in computational biology tend to have many groups making it difficult to distinguish between groups solely on color. Thus, this package is useful for increasing the accessibility of scatterplot visualizations to those with visual impairments such as color blindness.
	"""
	
	homepage = "https://github.com/FertigLab/scatterHatch"
	bioc = "scatterHatch" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/scatterHatch_1.8.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/scatterHatch/scatterHatch_1.8.0.tar.gz"]

	version("1.8.0", md5="d86cfd4fa0820f65efd6085edc997eed")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-spatstat-geom", type=("build", "run"))
