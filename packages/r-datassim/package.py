# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDatassim(RPackage):
	"""Data Assimilation

	For estimation of a variable of interest using Kalman filter by incorporating results from previous assessments, i.e. through development weighted estimates where weights are assigned inversely proportional to the variance of existing and new estimates. For reference see Ehlers et al. (2017) <doi:10.20944/preprints201710.0098.v1>.
	"""
	
	cran = "DatAssim" 

	version("1.0", md5="584a18d5da19eb22b8798509134abec1")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
