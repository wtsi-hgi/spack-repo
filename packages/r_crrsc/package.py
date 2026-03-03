# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCrrsc(RPackage):
	"""Competing Risks Regression for Stratified and Clustered Data

	Extension of 'cmprsk' to Stratified and Clustered data.    
      A goodness of fit test for Fine-Gray model is also provided.        
      Methods are detailed in the following articles: Zhou et al. (2011) <doi:10.1111/j.1541-0420.2010.01493.x>,
      Zhou et al. (2012) <doi:10.1093/biostatistics/kxr032>, 
      Zhou et al. (2013) <doi: 10.1002/sim.5815>.
	"""
	
	cran = "crrSC" 

	version("1.1.2", md5="bf9653270209e73c4637e76a84ee54e6")

	depends_on("r-survival", type=("build", "run"))
