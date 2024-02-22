# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REgrni(RPackage):
	"""Ensemble Gene Regulatory Network Inference

	Gene regulatory network constructed using combined score obtained from 
  individual network inference method. The combined score measures the significance 
  of edges in the ensemble network. Fisher's weighted method has been implemented to 
  combine the outcomes of different methods based on the probability values. 
  The combined score follows chi-square distribution with 2n degrees of freedom. <doi:10.22271/09746315.2020.v16.i3.1358>.
	"""
	
	cran = "EGRNi" 

	version("0.1.6", md5="4c9c2ab1a5c057ec08a917ee1c363a04")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-fdrtool", type=("build", "run"))
	depends_on("r-gdata", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
