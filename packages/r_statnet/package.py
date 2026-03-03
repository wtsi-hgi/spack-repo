# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStatnet(RPackage):
	"""Software Tools for the Statistical Analysis of Network Data

	Statnet is a collection of packages for statistical network analysis that are 
  designed to work together because they share common data representations and 'API' 
  design.  They provide an integrated set of tools for the representation, 
  visualization, analysis, and simulation of many different forms of network data.  
  This package is designed to make it easy to install and load the 
  key 'statnet' packages in a single step.  Learn more about 'statnet' 
  at <http://www.statnet.org>.  Tutorials for many packages can be found 
  at <https://github.com/statnet/Workshops/wiki>.  For an introduction to functions in this package, 
  type help(package='statnet').
	"""
	
	homepage = "http://statnet.org"
	cran = "statnet" 

	version("2019.6", md5="8dede6120d66b1a2962e070e8b3c4b8d")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-tergm@3.6.1:", type=("build", "run"))
	depends_on("r-ergm-count@3.3:", type=("build", "run"))
	depends_on("r-sna@2.4:", type=("build", "run"))
	depends_on("r-tsna@0.3:", type=("build", "run"))
	depends_on("r-ergm@3.10.4:", type=("build", "run"))
	depends_on("r-network@1.15:", type=("build", "run"))
	depends_on("r-networkdynamic@0.10:", type=("build", "run"))
	depends_on("r-statnet-common@4.2:", type=("build", "run"))
