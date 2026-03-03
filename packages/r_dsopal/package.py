# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDsopal(RPackage):
	"""'DataSHIELD' Implementation for 'Opal'

	'DataSHIELD' is an infrastructure and series of R packages that 
    enables the remote and 'non-disclosive' analysis of sensitive research data.
    This package is the 'DataSHIELD' interface implementation for 'Opal', which is
    the data integration application for biobanks by 'OBiBa'. Participant data, once
    collected from any data source, must be integrated and stored in a central
    data repository under a uniform model. 'Opal' is such a central repository.
    It can import, process, validate, query, analyze, report, and export data.
    'Opal' is the reference implementation of the 'DataSHIELD' infrastructure.
	"""
	
	homepage = "https://github.com/datashield/DSOpal/"
	cran = "DSOpal" 

	version("1.4.0", md5="d36e04139defa17c0d1e4bada199a8b9")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-opalr@3:", type=("build", "run"))
	depends_on("r-dsi@1.5:", type=("build", "run"))
