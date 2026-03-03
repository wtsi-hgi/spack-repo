# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDrf(RPackage):
	"""Distributional Random Forests

	An implementation of distributional random forests as introduced in Cevid & Michel & Meinshausen & Buhlmann (2020) <arXiv:2005.14458>.
	"""
	
	homepage = "https://github.com/lorismichel/drf"
	cran = "drf" 

	version("1.1.0", md5="efcd1561f71a10071b1580665faf7c6a")

	depends_on("r@3.4.4:", type=("build", "run"))
	depends_on("r-fastdummies", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-transport", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
