# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBrendadb(RPackage):
	"""The BRENDA Enzyme Database

	R interface for importing and analyzing enzyme information from the BRENDA database.
	"""
	
	homepage = "https://github.com/y1zhou/brendaDb"
	bioc = "brendaDb" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/brendaDb_1.16.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/brendaDb/brendaDb_1.16.0.tar.gz"]

	version("1.16.0", md5="35e521feef3f87b0122ac00ad0deae5b")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-biocfilecache", type=("build", "run"))
	depends_on("r-rappdirs", type=("build", "run"))
