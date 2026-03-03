# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDatamaid(RPackage):
	"""A Suite of Checks for Identification of Potential Errors in a
Data Frame as Part of the Data Screening Process

	Data screening is an important first step of any statistical
    analysis. dataMaid auto generates a customizable data report with a thorough
    summary of the checks and the results that a human can use to identify possible
    errors. It provides an extendable suite of test for common potential
    errors in a dataset. 
	"""
	
	homepage = "https://github.com/ekstroem/dataMaid"
	cran = "dataMaid" 

	version("1.4.1", md5="54e8d15b22b200c1096c4b342485b861")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-haven", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-pander", type=("build", "run"))
	depends_on("r-rmarkdown@1.10:", type=("build", "run"))
	depends_on("r-robustbase@0.93.2:", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-whoami", type=("build", "run"))
	depends_on("pandoc@2.0:", type=("build", "link", "run"))
	depends_on("git", type=("build", "link", "run"))
