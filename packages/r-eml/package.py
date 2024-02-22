# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REml(RPackage):
	"""Read and Write Ecological Metadata Language Files

	Work with Ecological Metadata Language ('EML') files. 
    'EML' is a widely used metadata standard in the ecological and
    environmental sciences, described in Jones et al. (2006),
    <doi:10.1146/annurev.ecolsys.37.091305.110031>.
	"""
	
	homepage = "https://docs.ropensci.org/EML/"
	cran = "EML" 

	version("2.0.6.1", md5="7748465e3917cc2cebfc2de2fe128684")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-emld@0.5:", type=("build", "run"))
	depends_on("r-jqr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-uuid", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
