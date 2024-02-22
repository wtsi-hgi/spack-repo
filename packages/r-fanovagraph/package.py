# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFanovagraph(RPackage):
	"""Building Kriging Models from FANOVA Graphs

	Estimation and plotting of a function's FANOVA graph to identify the interaction structure and fitting, prediction and simulation of a Kriging model modified by the identified structure. The interactive function plotManipulate() can only be run on the 'RStudio IDE' with 'RStudio' package 'manipulate' loaded. 'RStudio' is freely available (<https://rstudio.com/>), and includes package 'manipulate'. The equivalent function plotTk() bases on CRAN Repository packages only. For further information on the method see Fruth, J., Roustant, O., Kuhnt, S. (2014) <doi:10.1016/j.jspi.2013.11.007>. 
	"""
	
	cran = "fanovaGraph" 

	version("1.5", md5="316eccca6109dccd37c284e8dcd2d20c")

	depends_on("r-sensitivity", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-dicekriging@1.4:", type=("build", "run"))
