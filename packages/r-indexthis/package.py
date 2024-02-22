# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIndexthis(RPackage):
	"""Quick Indexation

	Quick indexation of any type of vector or of any combination of those. Indexation turns a vector into an integer vector going from 1 to the number of unique elements. Indexes are important building blocks for many algorithms. The method is described at <https://github.com/lrberge/indexthis/>.
	"""
	
	homepage = "https://github.com/lrberge/indexthis"
	cran = "indexthis" 

	version("1.0.1", md5="596fd585106ca220e9fb7f17e82d9309")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
