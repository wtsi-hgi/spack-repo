# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRedcapcast(RPackage):
	"""REDCap Castellated Data Handling

	Originally forked from the R part of 'REDCapRITS' by Paul Egeler. 
    See <https://github.com/pegeler/REDCapRITS>.
    'REDCap' database casting and handling of castellated data when using 
    repeated instruments and longitudinal projects. Keeps a focused data export 
    approach, by allowing to only export required data from the database.
    'REDCap' (Research Electronic Data Capture) is a secure, web-based software
    platform designed to support data capture for research studies, providing
    1) an intuitive interface for validated data capture; 2) audit trails for
    tracking data manipulation and export procedures; 3) automated export
    procedures for seamless data downloads to common statistical packages; and
    4) procedures for data integration and interoperability with external 
    sources (Harris et al (2009) <doi:10.1016/j.jbi.2008.08.010>; 
    Harris et al (2019) <doi:10.1016/j.jbi.2019.103208>).
	"""
	
	homepage = "https://github.com/agdamsbo/REDCapCAST"
	cran = "REDCapCAST" 

	version("24.2.1", md5="d00903e774a8af09176c8b6ed1020516")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-redcapr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-keyring", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-openxlsx2", type=("build", "run"))
	depends_on("r-rsconnect", type=("build", "run"))
	depends_on("r-haven", type=("build", "run"))
