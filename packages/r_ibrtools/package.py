# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIbrtools(RPackage):
	"""Integrating Biomarker-Based Assessments and Radarchart Creation

	Several functions to calculate two important indexes (IBR (Integrated Biomarker Response) and IBRv2 (Integrated Biological Response version 2)), it also calculates the standardized values for enzyme activity for each index, and it has a graphing function to perform radarplots that make great data visualization for this type of data. Beliaeff, B., & Burgeot, T. (2002). <https://pubmed.ncbi.nlm.nih.gov/12069320/>. Sanchez, W., Burgeot, T., & Porcher, J.-M. (2013).<doi:10.1007/s11356-012-1359-1>. Devin, S., Burgeot, T., Giambérini, L., Minguez, L., & Pain-Devin, S. (2014). <doi:10.1007/s11356-013-2169-9>. Minato N. (2022). <https://minato.sip21c.org/msb/>.
	"""
	
	cran = "IBRtools" 

	version("0.1.3", md5="3613203c0fe56a799a22cba8492713f3")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr@1.0.6:", type=("build", "run"))
	depends_on("r-tibble@3.0.4:", type=("build", "run"))
	depends_on("r-data-table@1.13.2:", type=("build", "run"))
	depends_on("r-gtools@3.9:", type=("build", "run"))
	depends_on("r-tidyr@1.1.3:", type=("build", "run"))
	depends_on("r-fmsb@0.7.1:", type=("build", "run"))
	depends_on("r-binhf@1.0.3:", type=("build", "run"))
	depends_on("r-tidyselect@1.2:", type=("build", "run"))
