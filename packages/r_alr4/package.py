# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAlr4(RPackage):
	"""Data to Accompany Applied Linear Regression 4th Edition

	Datasets to Accompany S. Weisberg (2014, ISBN: 978-1-118-38608-8), 
 "Applied Linear Regression," 4th edition.  Many data files 
 in this package are included in the `alr3` package as well, so only one of them 
 should be used.
	"""
	
	homepage = "http://www.z.umn.edu/alr4ed"
	cran = "alr4" 

	version("1.0.6", md5="e048ae41fd58f7b1ba9f7d8095b23308", url="https://cran.r-project.org/src/contrib/alr4_1.0.6.tar.gz")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
	depends_on("r-effects", type=("build", "run"))
