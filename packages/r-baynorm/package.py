# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBaynorm(RPackage):
	"""Single-cell RNA sequencing data normalization

	bayNorm is used for normalizing single-cell RNA-seq data.
	"""
	
	homepage = "https://github.com/WT215/bayNorm"
	bioc = "bayNorm" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/bayNorm_1.20.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/bayNorm/bayNorm_1.20.0.tar.gz"]

    version("1.26.0", tag="RELEASE_3_21")
	version("1.20.0", sha256="d8c553aca41a9b23a5e5a9b1973f7e73b717b28633e2dc7472a30fd203279b06")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-bb", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-iterators", type=("build", "run"))
	depends_on("r-dosnow", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-locfit", type=("build", "run"))
	depends_on("r-fitdistrplus", type=("build", "run"))
	depends_on("r-singlecellexperiment", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-rcppprogress", type=("build", "run"))
