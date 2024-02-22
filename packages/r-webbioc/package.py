# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWebbioc(RPackage):
	"""Bioconductor Web Interface

	An integrated web interface for doing microarray analysis using several of the Bioconductor packages. It is intended to be deployed as a centralized bioinformatics resource for use by many users. (Currently only Affymetrix oligonucleotide analysis is supported.)
	"""
	
	homepage = "http://www.bioconductor.org/"
	bioc = "webbioc" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/webbioc_1.74.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/webbioc/webbioc_1.74.0.tar.gz"]

	version("1.74.0", md5="59774accefb60098cdf15cfcd1cda508")

	depends_on("r@1.8:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-affy", type=("build", "run"))
	depends_on("r-multtest", type=("build", "run"))
	depends_on("r-annaffy", type=("build", "run"))
	depends_on("r-vsn", type=("build", "run"))
	depends_on("r-gcrma", type=("build", "run"))
	depends_on("r-qvalue", type=("build", "run"))
	depends_on("r-biocmanager", type=("build", "run"))
	depends_on("perl@5.6.0:", type=("build", "link", "run"))
	depends_on("netpbm", type=("build", "link", "run"))
