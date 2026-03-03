# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNnt(RPackage):
	"""The Number Needed to Treat (NNT) for Survival Endpoint

	Estimate the NNT using the proposed method in Yang and Yin's paper (2019)
  <doi:10.1371/journal.pone.0223301>, in which the NNT-RMST (number needed to 
  treat based on the restricted mean survival time) is defined as the RMST (restricted 
  mean survival time) in the control group divided by the difference in RMSTs 
  between the treatment and control groups up to a chosen time t.
	"""
	
	cran = "nnt" 

	version("0.1.4", md5="5cbed2ad1fe871d7518009e9bdc17ed2")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-survrm2", type=("build", "run"))
