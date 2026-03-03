# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTextdata(RPackage):
	"""Download and Load Various Text Datasets

	Provides a framework to download, parse, and store text
    datasets on the disk and load them when needed. Includes various
    sentiment lexicons and labeled text data sets for classification and
    analysis.
	"""
	
	homepage = "https://github.com/EmilHvitfeldt/textdata"
	cran = "textdata" 

	version("0.4.4", md5="c5072c1ab811e2bb9df7820885e69849")

	depends_on("r-fs", type=("build", "run"))
	depends_on("r-rappdirs", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
