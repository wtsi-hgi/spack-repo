# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStratigrapher(RPackage):
	"""Integrated Stratigraphy

	Includes bases for litholog generation: graphical functions
    based on R base graphics, interval management functions and svg importation 
    functions among others. Also include stereographic projection functions, 
    and other functions made to deal with large datasets while keeping options
    to get into the details of the data.
    When using for publication please cite 
    Sebastien Wouters, Anne-Christine Da Silva, Frederic Boulvain and 
    Xavier Devleeschouwer, 2021. The R Journal 13:2, 153-178.
    The palaeomagnetism functions are based on:
    Tauxe, L., 2010. Essentials of Paleomagnetism. University of California 
    Press. <https://earthref.org/MagIC/books/Tauxe/Essentials/>;
    Allmendinger, R. W., Cardozo, N. C., and Fisher, D., 2013, Structural 
    Geology Algorithms: Vectors & Tensors: Cambridge, England, Cambridge
    University Press, 289 pp.;
    Cardozo, N., and Allmendinger, R. W., 2013, Spherical projections
    with OSXStereonet: Computers & Geosciences, v. 51, no. 0, p. 193 - 205,
    <doi: 10.1016/j.cageo.2012.07.021>.
	"""
	
	cran = "StratigrapheR" 

	version("1.3.1", md5="ab6cec16dc82f102b1d7fafbb68eac41")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-diagram", type=("build", "run"))
	depends_on("r-reshape", type=("build", "run"))
