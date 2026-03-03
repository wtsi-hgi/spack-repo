# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNewsmap(RPackage):
	"""Semi-Supervised Model for Geographical Document Classification

	Semissupervised model for geographical document classification (Watanabe 2018) <doi:10.1080/21670811.2017.1293487>. 
    This package currently contains seed dictionaries in English, German, French, Spanish, Italian, Russian, Hebrew, Arabic Japanese and Chinese (Simplified and Traditional).
	"""
	
	homepage = "https://github.com/koheiw/newsmap"
	cran = "newsmap" 

	version("0.8.3", md5="4c2ae59005b9e5da6141addf4c271971")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-quanteda@2.1:", type=("build", "run"))
	depends_on("r-quanteda-textstats", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
