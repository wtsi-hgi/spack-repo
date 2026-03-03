# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBdpar(RPackage):
	"""Big Data Preprocessing Architecture

	
        Provide a tool to easily build customized data flows to pre-process large volumes 
    of information from different sources. To this end, 'bdpar' allows to (i) easily use and 
    create new functionalities and (ii) develop new data source extractors according to the 
    user needs. Additionally, the package provides by default a predefined data flow 
    to extract and pre-process the most relevant information (tokens, dates, ... ) from some textual 
    sources (SMS, Email, YouTube comments).
	"""
	
	homepage = "https://github.com/miferreiro/bdpar"
	cran = "bdpar" 

	version("3.1.0", md5="302c71f91537643958cacd1345696d09")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-rlist", type=("build", "run"))
	depends_on("python@3.6:", type=("build", "link", "run"))
