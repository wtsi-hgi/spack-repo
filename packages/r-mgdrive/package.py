# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMgdrive(RPackage):
	"""Mosquito Gene Drive Explorer

	Provides a model designed to be a reliable testbed where various gene 
    drive interventions for mosquito-borne diseases control. It is being developed to 
    accommodate the use of various mosquito-specific gene drive systems within a 
    population dynamics framework that allows migration of individuals between patches 
    in landscape. Previous work developing the population dynamics can be found in Deredec et al. 
    (2001) <doi:10.1073/pnas.1110717108> and Hancock & Godfray (2007) <doi:10.1186/1475-2875-6-98>, 
    and extensions to accommodate CRISPR homing dynamics in Marshall et al. (2017) 
    <doi:10.1038/s41598-017-02744-7>.
	"""
	
	homepage = "https://marshalllab.github.io/MGDrivE/"
	cran = "MGDrivE" 

	version("1.6.0", md5="08ba932e79bf5ce52d81ae19ba635087")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rdpack@0.7:", type=("build", "run"))
