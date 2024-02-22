# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNetlogor(RPackage):
	"""Build and Run Spatially Explicit Agent-Based Models

	Build and run spatially explicit
    agent-based models using only the R platform. 'NetLogoR' follows the same
    framework as the 'NetLogo' software
    (Wilensky (1999) <http://ccl.northwestern.edu/netlogo/>) and is a translation
    in R of the structure and functions of 'NetLogo'.
    'NetLogoR' provides new R classes to define model agents and functions to
    implement spatially explicit agent-based models in the R environment.
    This package allows benefiting of the fast and easy coding phase from the
    highly developed 'NetLogo' framework, coupled with the versatility, power
    and massive resources of the R software.
    Examples of two models from the NetLogo software repository 
    (Ants <http://ccl.northwestern.edu/netlogo/models/Ants>) and 
    Wolf-Sheep-Predation 
    (<http://ccl.northwestern.edu/netlogo/models/WolfSheepPredation>),
    and a third, Butterfly, from 
    Railsback and Grimm (2012) <https://www.railsback-grimm-abm-book.com/>, all
    written using 'NetLogoR' are available. 
    The 'NetLogo' code of the original version of these
    models is provided alongside.
    A programming guide inspired from the 'NetLogo' Programming Guide
    (<https://ccl.northwestern.edu/netlogo/docs/programming.html>) and a dictionary
    of 'NetLogo' primitives (<https://ccl.northwestern.edu/netlogo/docs/dictionary.html>)
    equivalences are also available.
    NOTE: To increment 'time', these functions can use a for loop or can be
    integrated with a discrete event simulator, such as 'SpaDES'
    (<https://cran.r-project.org/package=SpaDES>).
    The suggested package 'fastshp' can be installed with
    'install.packages("fastshp", repos = ("<https://rforge.net>"), type = "source")'.
	"""
	
	homepage = "https://netlogor.predictiveecology.org"
	cran = "NetLogoR" 

	version("1.0.5", md5="2519b11a78687ceb9a819d8114c66816")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-quickplot@1.0.2:", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
