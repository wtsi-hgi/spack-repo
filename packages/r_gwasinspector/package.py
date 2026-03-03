# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGwasinspector(RPackage):
	"""Comprehensive and Easy to Use Quality Control of GWAS Results

	When evaluating the results of a genome-wide association study (GWAS), it is important to perform a quality control to ensure that the results are valid, complete, correctly formatted, and, in case of meta-analysis, consistent with other studies that have applied the same analysis. This package was developed to facilitate and streamline this process and provide the user with a comprehensive report. 
	"""
	
	homepage = "http://GWASinspector.com"
	cran = "GWASinspector" 

	version("1.6.5", md5="ffec7e5f8a97dec350557e7c2d9420c3")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-ini@0.3:", type=("build", "run"))
	depends_on("r-futile-logger@1.4:", type=("build", "run"))
	depends_on("r-data-table@1.12.8:", type=("build", "run"))
	depends_on("r-hash@2.2:", type=("build", "run"))
	depends_on("r-ggplot2@3:", type=("build", "run"))
	depends_on("r-knitr@1.1:", type=("build", "run"))
	depends_on("r-rmarkdown@2.17:", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-rsqlite", type=("build", "run"))
	depends_on("r-kableextra@0.8:", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
	depends_on("r-openxlsx@4:", type=("build", "run"))
