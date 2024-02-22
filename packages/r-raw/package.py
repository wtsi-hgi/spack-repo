# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRaw(RPackage):
	"""R Actuarial Workshops

	In order to facilitate R instruction for actuaries, we have organized several 
  sets of publicly available data of interest to non-life actuaries. In addition, we suggest 
  a set of packages, which most practicing actuaries will use routinely. Finally, there is 
  an R markdown skeleton for basic reserve analysis.
	"""
	
	homepage = "http://casact.github.io/raw_package/"
	cran = "raw" 

	version("0.1.8", md5="3e7a16ffb44bd693f827a34279d85be4")

	depends_on("r@3.5:", type=("build", "run"))
