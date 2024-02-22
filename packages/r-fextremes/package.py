# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFextremes(RPackage):
	"""Rmetrics - Modelling Extreme Events in Finance

	Provides functions for analysing
  and modelling extreme events in financial time Series. The
  topics include: (i) data pre-processing, (ii) explorative 
  data analysis, (iii) peak over threshold modelling, (iv) block
  maxima modelling, (v) estimation of VaR and CVaR, and (vi) the
  computation of the extreme index.
	"""
	
	homepage = "https://www.rmetrics.org"
	cran = "fExtremes" 

	version("4032.84", md5="77f0bc1f4b0781beeb0b36fa91d68481")

	depends_on("r@2.15.1:", type=("build", "run"))
	depends_on("r-fbasics", type=("build", "run"))
	depends_on("r-fgarch", type=("build", "run"))
	depends_on("r-timedate", type=("build", "run"))
	depends_on("r-timeseries", type=("build", "run"))
