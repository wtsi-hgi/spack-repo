# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROhtadstats(RPackage):
	"""Tomoka Ohta D Statistics

	Calculate's Tomoka Ohta's partitioning of linkage disequilibrium,
 deemed D-statistics, for pairs of loci. Petrowski et al. (2019) <doi:10.5334/jors.250>.
	"""
	
	homepage = "https://github.com/pfpetrowski/OhtaDStats"
	cran = "ohtadstats" 

	version("2.1.1", md5="d457352f5a4304b005bd55cfd85b2e6b")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
