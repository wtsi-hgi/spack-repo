# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVisualize(RPackage):
	"""Graph Probability Distributions with User Supplied Parameters
and Statistics

	Graphs the pdf or pmf and highlights what area or probability is
    present in user defined locations. Visualize is able to provide lower tail,
    bounded, upper tail, and two tail calculations. Supports strict and equal
    to inequalities.  Also provided on the graph is the mean and variance of
    the distribution. 
	"""
	
	homepage = "https://github.com/coatless-rpkg/visualize"
	cran = "visualize" 

	version("4.5.0", md5="f3c53aa83ea5343079e74b7dce18045a")

	depends_on("r@4:", type=("build", "run"))
