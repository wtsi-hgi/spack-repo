# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTagcloud(RPackage):
	"""Tag Clouds

	Generating Tag and Word Clouds.
	"""
	
	homepage = "http://logfc.wordpress.com"
	cran = "tagcloud" 

	version("0.6", md5="8dea9f8fb29e81e72b32d062c77212fc")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
