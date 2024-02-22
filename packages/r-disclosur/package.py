# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDisclosur(RPackage):
	"""Text Conversion from Nexis Uni PDFs to R Data Frames

	Transform 'newswire' and earnings call transcripts as PDF obtained from 'Nexis Uni' to R data frames. Various 'newswires' and 'FairDisclosure' earnings call formats are supported. Further, users can apply several pre-defined dictionaries on the data based on Graffin et al. (2016)<doi:10.5465/amj.2013.0288> and Gamache et al. (2015)<doi:10.5465/amj.2013.0377>.
	"""
	
	cran = "disclosuR" 

	version("0.6.0", md5="33f5d22a36fd96ea8ef19db0c3f9c3e2")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-pdftools", type=("build", "run"))
	depends_on("r-qdap", type=("build", "run"))
	depends_on("r-sentimentanalysis", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-syuzhet", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-snowballc", type=("build", "run"))
	depends_on("r-tm", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
