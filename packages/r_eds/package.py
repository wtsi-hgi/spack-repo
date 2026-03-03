# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REds(RPackage):
	"""eds: Low-level reader for Alevin EDS format

	This packages provides a single function, readEDS. This is a low-level utility for reading in Alevin EDS format into R. This function is not designed for end-users but instead the package is predominantly for simplifying package dependency graph for other Bioconductor packages.
	"""
	
	homepage = "https://github.com/mikelove/eds"
	bioc = "eds" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/eds_1.4.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/eds/eds_1.4.0.tar.gz"]

	version("1.4.0", md5="5992ff2692afb665a65bc9755175de5c")

	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("zlib", type=("build", "link", "run"))
