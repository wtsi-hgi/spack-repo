# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcssplot(RPackage):
	"""Styling of Graphics using Cascading Style Sheets

	Provides a means to style plots through cascading style sheets.
    This separates the aesthetics from the data crunching in plots and charts.
	"""
	
	homepage = "https://github.com/tkonopka/Rcssplot"
	cran = "Rcssplot" 

	version("1.0.0", md5="147c564da3d9d30f77cea787643a6dba")

	depends_on("r@3.4:", type=("build", "run"))
