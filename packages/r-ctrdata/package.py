# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCtrdata(RPackage):
	"""Retrieve and Analyze Clinical Trials in Public Registers

	A system for querying, retrieving and analyzing
        protocol- and results-related information on clinical trials from
        four public registers, the 'European Union Clinical Trials Register'
        ('EUCTR', <https://www.clinicaltrialsregister.eu/>), 
        'ClinicalTrials.gov' ('CTGOV', using the classic interface at 
        <https://classic.clinicaltrials.gov/>, and 'CTGOV2', using the 
        current interface at <https://www.clinicaltrials.gov/>), the 
        'ISRCTN' (<http://www.isrctn.com/>) and the
        'European Union Clinical Trials Information System'
        ('CTIS', <https://euclinicaltrials.eu/>). 
        Trial information is downloaded, converted and stored in a database 
        ('PostgreSQL', 'SQLite', 'DuckDB' or 'MongoDB'; via package 'nodbi'). 
        Documents in registers associated with trials can also be downloaded. 
        Other functions identify deduplicated records, 
        easily find and extract variables (fields) of interest even 
        from complex nested data as used by the registers, 
        merge variables and update queries. 
        The package can be used for meta-analysis and trend-analysis of
        the design and conduct as well as of the results of clinical trials.
	"""
	
	homepage = "https://cran.r-project.org/package=ctrdata"
	cran = "ctrdata" 

	version("1.17.2", md5="dce24b29e61071bd0824193b59b9b1dc")

	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-curl@5.1:", type=("build", "run"))
	depends_on("r-clipr", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-nodbi@0.10:", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-jqr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-zip", type=("build", "run"))
	depends_on("r-v8", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
