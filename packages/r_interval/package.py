# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RInterval(RPackage):
	"""Weighted Logrank Tests and NPMLE for Interval Censored Data

	Functions to fit nonparametric survival curves, plot them, and perform logrank or Wilcoxon type tests [see Fay and Shaw <doi:10.18637/jss.v036.i02>].
	"""
	
	cran = "interval" 

	version("1.1-1.0", md5="f7cdec464d2647aac4d76709df5ffda5")

	depends_on("r@2.2.1:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-perm@1:", type=("build", "run"))
	depends_on("r-icens", type=("build", "run"))
	depends_on("r-mlecens", type=("build", "run"))
