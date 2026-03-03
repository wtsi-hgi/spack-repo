# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSmoothy(RPackage):
	"""Automatic Estimation of the Most Likely Drug Combination using
Smooth Algorithm

	A flexible moving average algorithm for modeling drug exposure in pharmacoepidemiology studies as presented in the article: Ouchi, D.,  Giner-Soriano, M., Gómez-Lumbreras, A., Vedia Urgell, C.,Torres, F., & Morros, R. (2022). "Automatic Estimation of the Most Likely Drug Combination in Electronic Health Records Using the Smooth Algorithm : Development and Validation Study." JMIR medical informatics, 10(11), e37976. <doi:10.2196/37976>.
	"""
	
	cran = "smoothy" 

	version("1.0.0", md5="cb7d1818cbe715117c0cf2353121bd5a")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr@1.3:", type=("build", "run"))
	depends_on("r-zoo@1.8:", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
