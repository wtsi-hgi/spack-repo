# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMatur(RPackage):
	"""Athlete Maturation and Biobanding

	Identifying maturation stages across young athletes is paramount for talent identification. Furthermore, the concept of biobanding, or grouping of athletes based on their biological development, instead of their chronological age, has been widely researched. The goal of this package is to help professionals working in the field of strength & conditioning and talent ID obtain common maturation metrics and as well as to quickly visualize this information via several plotting options. For the methods behind the computed maturation metrics implemented in this package refer to Khamis, H. J., & Roche, A. F. (1994) <https://pubmed.ncbi.nlm.nih.gov/7936860/>, Mirwald, R.L et al., (2002) <https://pubmed.ncbi.nlm.nih.gov/11932580/> and Cumming, Sean P. et al., (2017) <doi:10.1519/SSC.0000000000000281>. 
	"""
	
	homepage = "https://github.com/josedv82/matuR"
	cran = "matuR" 

	version("0.0.1.0", md5="9f33537812e5853a756f3d2edcf5abf1")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
