# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RR62s3(RPackage):
	"""Automatic Method Generation from R6

	After defining an R6 class, R62S3 is used to automatically generate optional S3/S4 generics and methods for dispatch. Also allows piping for R6 objects.
	"""
	
	homepage = "https://github.com/RaphaelS1/R62S3/"
	cran = "R62S3" 

	version("1.4.1", md5="6f006522e03b883adbefeb76eb18072a", url="https://cran.r-project.org/src/contrib/R62S3_1.4.1.tar.gz")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
