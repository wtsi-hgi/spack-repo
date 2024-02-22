# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgmatplot(RPackage):
	"""Plot Columns of Two Matrices Against Each Other Using 'ggplot2'

	A quick and easy way of plotting the columns of two matrices or 
    data frames against each other using 'ggplot2'. Although 'ggmatplot' doesn't 
    provide the same flexibility as 'ggplot2', it can be used as a workaround for 
    having to wrangle wide format data into long format for plotting with
    'ggplot2'.
	"""
	
	homepage = "https://github.com/xuan-liang/ggmatplot"
	cran = "ggmatplot" 

	version("0.1.2", md5="579210b6cc06d72becc306bb7c869642")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
