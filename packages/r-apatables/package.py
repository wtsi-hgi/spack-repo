# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RApatables(RPackage):
	"""Create American Psychological Association (APA) Style Tables

	A common task faced by researchers is the creation of APA style
    (i.e., American Psychological Association style) tables from statistical
    output. In R a large number of function calls are often needed to obtain all of
    the desired information for a single APA style table. As well, the process of
    manually creating APA style tables in a word processor is prone to transcription
    errors. This package creates Word files (.doc files) containing APA style tables
    for several types of analyses. Using this package minimizes transcription errors
    and reduces the number commands needed by the user.
	"""
	
	homepage = "https://github.com/dstanley4/apaTables"
	cran = "apaTables" 

	version("2.0.8", md5="fd5efafa96db946433eae066e181dc67")

	depends_on("r@3.1.2:", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
	depends_on("r-broom", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-mbess", type=("build", "run"))
