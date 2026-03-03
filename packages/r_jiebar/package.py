# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJiebar(RPackage):
	"""Chinese Text Segmentation

	Chinese text segmentation, keyword extraction and speech tagging
    For R.
	"""
	
	homepage = "https://github.com/qinwf/jiebaR/"
	cran = "jiebaR" 

	version("0.11", md5="2717f8b316e04ef7a52f2f359470b834")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-jiebard", type=("build", "run"))
	depends_on("r-rcpp@0.12.1:", type=("build", "run"))
