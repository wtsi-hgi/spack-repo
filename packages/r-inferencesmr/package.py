# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RInferencesmr(RPackage):
	"""Inference About the Standardized Mortality Ratio when Evaluating
the Effect of a Screening Program on Survival

	Functions to make inference about the 
        standardized mortality ratio (SMR) when evaluating the
        effect of a screening program. The package is
        based on methods described in Sasieni (2003) 
        <doi: 10.1097/00001648-200301000-00026> and 
        Talbot et al. (2011) <doi: 10.1002/sim.4334>.
	"""
	
	cran = "InferenceSMR" 

	version("1.0.2", md5="b9fec2c75222da59c71f85c1a07a950c")

	depends_on("r-survival", type=("build", "run"))
