# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHeims(RPackage):
	"""Decode and Validate HEIMS Data from Department of Education,
Australia

	Decode elements of the Australian Higher Education Information Management System (HEIMS) data for clarity and performance. HEIMS is the record system of the Department of Education, Australia to record enrolments and completions in Australia's higher education system, as well as a range of relevant information. For more information, including the source of the data dictionary, see <http://heimshelp.education.gov.au/sites/heimshelp/dictionary/pages/data-element-dictionary>.
	"""
	
	cran = "heims" 

	version("0.4.0", md5="d0cf19331f176698bf0151b7a71ed010")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-hutils", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-fastmatch", type=("build", "run"))
	depends_on("r-bit64", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
