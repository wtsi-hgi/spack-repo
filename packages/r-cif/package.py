# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCif(RPackage):
	"""Cointegrated ICU Forecasting

	Set of forecasting tools to predict ICU beds using a Vector Error Correction model with a single cointegrating vector. Method described in  Berta, P. Lovaglio, P.G. Paruolo, P. Verzillo, S., 2020. "Real Time Forecasting of Covid-19 Intensive Care Units demand" Health, Econometrics and Data Group (HEDG) Working Papers 20/16, HEDG, Department of Economics, University of York, <https://www.york.ac.uk/media/economics/documents/hedg/workingpapers/2020/2016.pdf>. 
	"""
	
	cran = "cif" 

	version("0.1.1", md5="2ac1b527cda2e2e9f5da450315c8516b")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
