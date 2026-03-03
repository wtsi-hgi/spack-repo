# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMapfit(RPackage):
	"""PH/MAP Parameter Estimation

	Estimation methods for phase-type
  distribution (PH) and Markovian arrival process (MAP) from
  empirical data (point and grouped data) and density function.
  The tool is based on the following researches:
  Okamura et al. (2009) <doi:10.1109/TNET.2008.2008750>,
  Okamura and Dohi (2009) <doi:10.1109/QEST.2009.28>,
  Okamura et al. (2011) <doi:10.1016/j.peva.2011.04.001>,
  Okamura et al. (2013) <doi:10.1002/asmb.1919>,
  Horvath and Okamura (2013) <doi:10.1007/978-3-642-40725-3_10>,
  Okamura and Dohi (2016) <doi:10.15807/jorsj.59.72>.
	"""
	
	homepage = "https://github.com/okamumu/mapfit"
	cran = "mapfit" 

	version("1.0.0", md5="f00cba715318f853e41566a88a6a25e5")

	depends_on("r-r6", type=("build", "run"))
	depends_on("r-deformula", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
