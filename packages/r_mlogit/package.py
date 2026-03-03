# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMlogit(RPackage):
	"""Multinomial Logit Models

	Maximum likelihood estimation of random utility discrete
             choice models. The software is described in Croissant (2020)
              <doi:10.18637/jss.v095.i11> and the underlying methods in
              Train (2009) <doi:10.1017/CBO9780511805271>.
	"""
	
	homepage = "https://cran.r-project.org/package=mlogit"
	cran = "mlogit" 

	version("1.1-1", md5="08c4273d0762bd0044cf6677c927df9b")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dfidx", type=("build", "run"))
	depends_on("r-formula", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-lmtest", type=("build", "run"))
	depends_on("r-statmod", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
