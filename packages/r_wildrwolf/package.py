# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWildrwolf(RPackage):
	"""Fast Computation of Romano-Wolf Corrected p-Values for Linear
Regression Models

	Fast Routines to Compute Romano-Wolf corrected p-Values 
             (Romano and Wolf (2005a) <DOI:10.1198/016214504000000539>, 
             Romano and Wolf (2005b) <DOI:10.1111/j.1468-0262.2005.00615.x>) 
             for objects of type 'fixest' and 'fixest_multi' from the 'fixest' 
             package via a wild (cluster) bootstrap.
	"""
	
	homepage = "https://s3alfisc.github.io/wildrwolf/"
	cran = "wildrwolf" 

	version("0.6.1", md5="acf9dbe4fc51c94b0deaf27812f6f428")

	depends_on("r-fixest", type=("build", "run"))
	depends_on("r-fwildclusterboot", type=("build", "run"))
	depends_on("r-dreamerr", type=("build", "run"))
	depends_on("r-fabricatr", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
