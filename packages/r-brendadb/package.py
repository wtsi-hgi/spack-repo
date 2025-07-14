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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/brendaDb_1.16.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/brendaDb/brendaDb_1.16.0.tar.gz"]

    version("1.22.0", tag="RELEASE_3_21")
	version("1.16.0", sha256="1ea1ce49d64ab74770811353e97585d59e4664afa88c21c8272fbbf1b9314dc3")

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
