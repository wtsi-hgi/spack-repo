# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRecorder(RPackage):
	"""Toolkit to Validate New Data for a Predictive Model

	A lightweight toolkit to validate new observations when computing
    their predictions with a predictive model. The validation process 
    consists of two steps: (1) record relevant statistics and meta data of the
    variables in the original training data for the predictive model and
    (2) use these data to run a set of basic validation tests on the new set of 
    observations.
	"""
	
	homepage = "https://github.com/smaakage85/recorder"
	cran = "recorder" 

	version("0.8.2", md5="ad3b0ce0fbaf48626cfc6c8a469385f4")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
