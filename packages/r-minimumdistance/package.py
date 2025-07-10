# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMinimumdistance(RPackage):
	"""A Package for De Novo CNV Detection in Case-Parent Trios

	Analysis of de novo copy number variants in trios from high-dimensional genotyping platforms.
	"""
	
	bioc = "MinimumDistance" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/MinimumDistance_1.46.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/MinimumDistance/MinimumDistance_1.46.0.tar.gz"]

	version("1.46.0", sha256="3fee8e9245cf5264a9dc5582197b11381198bb13be565441a8019fd90b967bbd")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-vanillaice@1.47.1:", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-matrixgenerics", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-s4vectors@0.23.18:", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-genomicranges@1.17.16:", type=("build", "run"))
	depends_on("r-summarizedexperiment@1.15.4:", type=("build", "run"))
	depends_on("r-oligoclasses", type=("build", "run"))
	depends_on("r-dnacopy", type=("build", "run"))
	depends_on("r-ff", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
