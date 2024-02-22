# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLogib(RPackage):
	"""Salary Analysis by the Swiss Federal Office for Gender Equality

	Implementation of the Swiss Confederation's standard analysis model for salary analyses <https://www.ebg.admin.ch/dam/ebg/en/dokumente/lohngleichheit/infos-zu-analysen/standard-analysemodellzurueberpruefungderlohngleichheitzwischenf.pdf.download.pdf/methodological_approachformonitoringcompliancewithwageequalitybe.pdf> in R. The analysis is run at company-level and the model is intended for companies with 50 or more employees (apprentices, trainees/interns and expats are not included in the analysis). Employees with at least 100 employees are required by the Gender Equality Act to conduct an equal pay analysis.
    This package allows users to run the equal salary analysis in R, providing additional transparency with respect to the methodology and simple automation possibilities.
	"""
	
	cran = "logib" 

	version("0.1.2", md5="795a3636666f435b43c24afe2506fd9b")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-lubridate@1.7.9:", type=("build", "run"))
	depends_on("r-readxl@1.3.1:", type=("build", "run"))
