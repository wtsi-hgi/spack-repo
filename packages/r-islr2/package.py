# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIslr2(RPackage):
	"""Introduction to Statistical Learning, Second Edition

	We provide the collection of data-sets used in the book 'An Introduction to Statistical Learning with Applications in R, Second Edition'. These include many data-sets that we used in the first edition (some with minor changes), and some new datasets.
	"""
	
	homepage = "https://www.statlearning.com"
	cran = "ISLR2" 

	version("1.3-2", md5="6c58aeb69067e4c39ab7c3a133a64e8d", url="https://cran.r-project.org/src/contrib/ISLR2_1.3-2.tar.gz")

	depends_on("r@3.5:", type=("build", "run"))
