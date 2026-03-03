# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNeedmining(RPackage):
	"""A Simple Needmining Implementation

	Showcasing needmining (the semi-automatic extraction of customer needs from
	social media data) with Twitter data. It uses the handling of the Twitter API provided by
	the package 'rtweet' and the textmining algorithms provided by the package 'tm'.
	Niklas Kuehl (2016) <doi:10.1007/978-3-319-32689-4_14> wrote an introduction to the topic of needmining.
	"""
	
	cran = "needmining" 

	version("0.1.1", md5="39b6f2f8ff66052b78f284a711e29427")

	depends_on("r-rtweet", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-snowballc", type=("build", "run"))
	depends_on("r-sparsem", type=("build", "run"))
	depends_on("r-tau", type=("build", "run"))
	depends_on("r-tm", type=("build", "run"))
