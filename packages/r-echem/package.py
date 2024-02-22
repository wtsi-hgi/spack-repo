# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REchem(RPackage):
	"""Simulations for Electrochemistry Experiments

	Simulates cyclic voltammetry, linear-sweep voltammetry 
    (both with and without stirring of the solution), and single-pulse 
    and double-pulse chronoamperometry and chronocoulometry 
    experiments using the implicit finite difference method outlined in 
    Gosser (1993, ISBN: 9781560810261) and in Brown (2015) 
    <doi:10.1021/acs.jchemed.5b00225>. Additional functions provide 
    ways to display and to examine the results of these simulations.
    The primary purpose of this package is to provide tools for
    use in courses in analytical chemistry.
	"""
	
	homepage = "https://github.com/dtharvey/eChem"
	cran = "eChem" 

	version("1.0.0", md5="245bfaf475d4f5ab20ba0cee2600150f")

	depends_on("r-plot3d", type=("build", "run"))
	depends_on("r-animation", type=("build", "run"))
