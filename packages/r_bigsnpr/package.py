# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBigsnpr(RPackage):
	"""Analysis of Massive SNP Arrays

	Easy-to-use, efficient, flexible and scalable tools for analyzing 
    massive SNP arrays. Privé et al. (2018) <doi:10.1093/bioinformatics/bty185>.
	"""
	
	homepage = "https://privefl.github.io/bigsnpr/"
	cran = "bigsnpr" 

	version("1.12.2", md5="05ccbd2478020001cd9ff49510c97a41")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-bigstatsr", type=("build", "run"))
	depends_on("r-bigassertr@0.1.6:", type=("build", "run"))
	depends_on("r-bigparallelr", type=("build", "run"))
	depends_on("r-bigsparser", type=("build", "run"))
	depends_on("r-bigreadr", type=("build", "run"))
	depends_on("r-bigutilsr@0.3.3:", type=("build", "run"))
	depends_on("r-data-table@1.12.4:", type=("build", "run"))
	depends_on("r-dorng", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-matrix@1.3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-runonce@0.2.3:", type=("build", "run"))
	depends_on("r-vctrs", type=("build", "run"))
	depends_on("r-rcpparmadillo@0.9.600:", type=("build", "run"))
	depends_on("r-rmio", type=("build", "run"))
	depends_on("r-roptim@0.1.6:", type=("build", "run"))
	depends_on("zlib", type=("build", "link", "run"))
