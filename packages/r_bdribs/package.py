# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBdribs(RPackage):
	"""Bayesian Detection of Potential Risk Using Inference on Blinded
Safety Data

	Implements Bayesian inference to detect signal from blinded 
    clinical trial when total number of adverse events of special 
    concerns and total risk exposures from all patients are available in the study.  
    For more details see the article by Mukhopadhyay et. al. (2018) 
    titled 'Bayesian Detection of Potential Risk Using Inference on Blinded Safety Data', 
    in Pharmaceutical Statistics (to appear). 
	"""
	
	cran = "bdribs" 

	version("1.0.4", md5="8f1520e715b1e79c01bc6a8ade282549")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-rjags", type=("build", "run"))
