# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCorrectedfdr(RPackage):
	"""Correcting False Discovery Rates

	There are many estimators of false discovery rate. In this package we compute the Nonlocal False
   Discovery Rate (NFDR) and the estimators of local false discovery rate: Corrected False discovery
   Rate (CFDR), Re-ranked False Discovery rate (RFDR) and the blended estimator. 
   Bickel, D.R., Rahal, A. (2019) <https://tinyurl.com/kkdc9rk8>.
	"""
	
	cran = "CorrectedFDR" 

	version("1.1", md5="f89f42fc40dd437cc4f9c40d33d61c43")

	depends_on("r@2.14.2:", type=("build", "run"))
