# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
	
from spack.package import *
	
			
class RBigstatsr(RPackage):
	"""Statistical Tools for Filebacked Big Matrices

	Easy-to-use, efficient, flexible and scalable statistical tools.
  Package bigstatsr provides and uses Filebacked Big Matrices via memory-mapping.
  It provides for instance matrix operations, Principal Component Analysis,
  sparse linear supervised models, utility functions and more
  <doi:10.1093/bioinformatics/bty185>.
	"""
	
	homepage = "https://privefl.github.io/bigstatsr/"
	cran = "bigstatsr" 

	version("1.5.12", md5="5ab7b1cfa54fd88bd42889029182a158")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-bigassertr@0.1.1:", type=("build", "run"))
	depends_on("r-bigparallelr@0.2.3:", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-ggplot2@3.0:", type=("build", "run"))
	depends_on("r-ps@1.4:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rmio@0.4:", type=("build", "run"))
	depends_on("r-rspectra", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-rmio", type=("build", "run"))
