# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNearfar(RPackage):
	"""Near-Far Matching

	Near-far matching is a study design technique for preprocessing observational data to mimic a pair-randomized trial. Individuals are matched to be near on measured confounders and far on levels of an instrumental variable. Methods outlined in further detail in Rigdon, Baiocchi, and Basu (2018) <doi:10.18637/jss.v086.c05>. 
	"""
	
	cran = "nearfar" 

	version("1.3", md5="a464bc337edef94e6d27e5a5eda80fea")

	depends_on("r-nbpmatching", type=("build", "run"))
	depends_on("r-gensa", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
