# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBmemlavaan(RPackage):
	"""Mediation Analysis with Missing Data and Non-Normal Data

	Methods for mediation analysis with missing data and non-normal data are implemented. For missing data, four methods are available: Listwise deletion, Pairwise deletion, Multiple imputation, and Two Stage Maximum Likelihood algorithm. For MI and TS-ML, auxiliary variables can be included to handle missing data. For handling non-normal data, bootstrap and two-stage robust methods can be used. Technical details of the methods can be found in Zhang and Wang (2013, <doi:10.1007/s11336-012-9301-5>), Zhang (2014, <doi:10.3758/s13428-013-0424-0>), and Yuan and Zhang (2012, <doi:10.1007/s11336-012-9282-4>).
	"""
	
	homepage = "https://bigdatalab.nd.edu"
	cran = "bmemLavaan" 

	version("0.5", md5="2a92cc2a7281f1c585f85ae5a74175b1")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-amelia", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-snowfall", type=("build", "run"))
	depends_on("r-rsem", type=("build", "run"))
	depends_on("r-lavaan", type=("build", "run"))
	depends_on("r-sem", type=("build", "run"))
