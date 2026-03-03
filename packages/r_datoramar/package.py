# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDatoramar(RPackage):
	"""Interface to the 'Datorama' API

	A thin wrapper around the 'Datorama' API.
    Ideal for analyzing marketing data from <https://datorama.com>.
	"""
	
	homepage = "https://github.com/beigebrucewayne/datoramar"
	cran = "datoramar" 

	version("0.1.0", md5="5182ba83fc3bde5252cd1170baca2e94")

	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
