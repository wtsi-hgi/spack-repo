# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDaiquiri(RPackage):
	"""Data Quality Reporting for Temporal Datasets

	Generate reports that enable quick visual review of 
    temporal shifts in record-level data. Time series plots showing aggregated 
    values are automatically created for each data field (column) depending on its 
    contents (e.g. min/max/mean values for numeric data, no. of distinct 
    values for categorical data), as well as overviews for missing values, 
    non-conformant values, and duplicated rows. The resulting reports are shareable 
    and can contribute to forming a transparent record of the entire analysis process. 
    It is designed with Electronic Health Records in mind, but can be used for 
    any type of record-level temporal data (i.e. tabular data where each row represents 
    a single "event", one column contains the "event date", and other columns 
    contain any associated values for the event).
	"""
	
	homepage = "https://github.com/ropensci/daiquiri"
	cran = "daiquiri" 

	version("1.1.1", md5="a1b7116ee340c94c5f5689c8ad34d8cc")

	depends_on("r-data-table@1.12.8:", type=("build", "run"))
	depends_on("r-readr@2:", type=("build", "run"))
	depends_on("r-ggplot2@3.1:", type=("build", "run"))
	depends_on("r-scales@1.1:", type=("build", "run"))
	depends_on("r-cowplot@0.9.3:", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-reactable@0.2.3:", type=("build", "run"))
	depends_on("r-xfun@0.15:", type=("build", "run"))
