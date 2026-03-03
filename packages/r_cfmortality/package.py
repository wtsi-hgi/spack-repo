# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCfmortality(RPackage):
	"""Cystic Fibrosis Survival Prediction Model Based on Stanojevic
Model

	Allows clinicians to predict survival probabilities over the next two years for cystic fibrosis patients, based on the clinical prediction models published in Stanojevic et al. (2019) <doi:10.1183/13993003.00224-2019>.
	"""
	
	cran = "cfmortality" 

	version("0.3.0", md5="e8cce1da342db1dbfd68efc728cee971")

