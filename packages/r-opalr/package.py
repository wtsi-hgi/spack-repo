# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROpalr(RPackage):
	"""'Opal' Data Repository Client and 'DataSHIELD' Utils

	Data integration Web application for biobanks by 'OBiBa'. 'Opal' is
    the core database application for biobanks. Participant data, once
    collected from any data source, must be integrated and stored in a central
    data repository under a uniform model. 'Opal' is such a central repository.
    It can import, process, validate, query, analyze, report, and export data.
    'Opal' is typically used in a research center to analyze the data acquired at
    assessment centres. Its ultimate purpose is to achieve seamless
    data-sharing among biobanks. This 'Opal' client allows to interact with 'Opal'
    web services and to perform operations on the R server side. 'DataSHIELD'
    administration tools are also provided.
	"""
	
	homepage = "https://github.com/obiba/opalr/"
	cran = "opalr" 

	version("3.4.1", md5="642b80e825fd1e3160f27c1d52c043ff")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-mime", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-labelled", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
