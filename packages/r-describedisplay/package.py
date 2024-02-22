# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDescribedisplay(RPackage):
	"""An Interface to the 'DescribeDisplay' 'GGobi' Plugin

	Produce publication quality graphics from output of 'GGobi'
    describe display plugin.
	"""
	
	homepage = "https://github.com/ggobi/DescribeDisplay"
	cran = "DescribeDisplay" 

	version("0.2.11", md5="07d4d573139fecbc1f4a83af749ed937")

	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-ggplot2@3.4.1:", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-ggally@2.1.2:", type=("build", "run"))
