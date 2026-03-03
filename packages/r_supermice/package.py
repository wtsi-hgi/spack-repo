# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSupermice(RPackage):
	"""SuperLearner Method for MICE

	Adds a Super Learner ensemble model method (using the 'SuperLearner' package)  
    to the 'mice' package. Laqueur, H. S., Shev, A. B., Kagawa, R. M. C. (2021) <doi:10.1093/aje/kwab271>.
	"""
	
	cran = "superMICE" 

	version("1.1.1", md5="2d772c1f62e178b5a5cf690f8872b200")

	depends_on("r-mice", type=("build", "run"))
	depends_on("r-superlearner", type=("build", "run"))
