# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRextendr(RPackage):
	"""Call Rust Code from R using the 'extendr' Crate

	Provides functions to compile and load Rust code from R, similar
    to how 'Rcpp' or 'cpp11' allow easy interfacing with C++ code. Also provides
    helper functions to create R packages that use Rust code. Under the hood,
    the Rust crate 'extendr' is used to do all the heavy lifting.
	"""
	
	homepage = "https://extendr.github.io/rextendr/"
	cran = "rextendr" 

	version("0.3.1", md5="a95225979c799004c410bf9ff3bcd224")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-brio", type=("build", "run"))
	depends_on("r-callr", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-desc", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-pkgbuild@1.4:", type=("build", "run"))
	depends_on("r-processx", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang@1.0.5:", type=("build", "run"))
	depends_on("r-rprojroot", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-vctrs", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
	depends_on("rust", type=("build", "link", "run"))
