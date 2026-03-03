# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScaleboot(RPackage):
	"""Approximately Unbiased P-Values via Multiscale Bootstrap

	Calculating approximately unbiased (AU) p-values
	from multiscale bootstrap probabilities. See
	Shimodaira (2004) <doi:10.1214/009053604000000823>,
	Shimodaira (2008) <doi:10.1016/j.jspi.2007.04.001>, 
	Terada ans Shimodaira (2017) <arXiv:1711.00949>, and
	Shimodaira and Terada (2019) <doi.org/10.3389/fevo.2019.00174>.
	"""
	
	homepage = "http://stat.sys.i.kyoto-u.ac.jp/prog/scaleboot/"
	cran = "scaleboot" 

	version("1.0-1", md5="0c6647beec106511d9451f7d72335675")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-pvclust@2.2.0:", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
