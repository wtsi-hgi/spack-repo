# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCondusco(RPackage):
	"""Query-Driven Pipeline Execution and Query Templates

	Runs a function iteratively over each row of either a dataframe 
    or the results of a query.  Use the 'BigQuery' and 'DBI' wrappers to 
    iteratively pass each row of query results to a function.  If a field 
    contains a 'JSON' string, it will be converted to an object.  This is 
    helpful for queries that return 'JSON' strings that represent objects.  
    These fields can then be treated as objects by the pipeline.
	"""
	
	homepage = "https://github.com/ras44/condusco"
	cran = "condusco" 

	version("0.1.0", md5="3729eafc4408be7259706320b213c1a2")

	depends_on("r@3.3.2:", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-bigrquery", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
