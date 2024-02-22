# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRdomains(RPackage):
	"""Get the Category of Content Hosted by a Domain

	Get the category of content hosted by a domain. Use Shallalist <http://shalla.de/>,
    Virustotal (which provides access to lots of services) <https://www.virustotal.com/>,
    Alexa <https://aws.amazon.com/awis/>, DMOZ <https://curlie.org/>, University Domain list
    <https://github.com/Hipo/university-domains-list> or validated machine learning
    classifiers based on Shallalist data to learn about the kind of content hosted by a domain.
	"""
	
	cran = "rdomains" 

	version("0.2.1", md5="9871bb2831c2a7c99ae45244382b8a5e")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-urltools", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-virustotal", type=("build", "run"))
	depends_on("r-aws-alexa", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-devtools", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
