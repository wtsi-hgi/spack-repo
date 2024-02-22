# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgchernoff(RPackage):
	"""Chernoff Faces for 'ggplot2'

	Provides a Chernoff face geom for 'ggplot2'. Maps multivariate data
    to human-like faces. Inspired by Chernoff (1973) <doi:10.1080/01621459.1973.10482434>.
	"""
	
	homepage = "https://github.com/Selbosh/ggChernoff"
	cran = "ggChernoff" 

	version("0.3.0", md5="13955a368867b27354cee7a42dad3fb5")

	depends_on("r@3.2.5:", type=("build", "run"))
	depends_on("r-ggplot2@2.2:", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
