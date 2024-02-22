# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMkinfer(RPackage):
	"""Inferential Statistics

	Computation of various confidence intervals (Altman et al. (2000), ISBN:978-0-727-91375-3; Hedderich and Sachs (2018), ISBN:978-3-662-56657-2) including bootstrapped versions (Davison and Hinkley (1997), ISBN:978-0-511-80284-3) as well as Hsu (Hedderich and Sachs (2018), ISBN:978-3-662-56657-2), permutation (Janssen (1997), <doi:10.1016/S0167-7152(97)00043-6>), bootstrap (Davison and Hinkley (1997), ISBN:978-0-511-80284-3) and multiple imputation (Barnard and Rubin (1999), <doi:10.1093/biomet/86.4.948>) t-test and Wilcoxon tests. Graphical visualization by volcano and Bland-Altman plots (Bland and Altman (1986), <doi:10.1016/S0140-6736(86)90837-8>; Shieh (2018), <doi:10.1186/s12874-018-0505-y>).
	"""
	
	homepage = "https://github.com/stamats/MKinfer"
	cran = "MKinfer" 

	version("1.1", md5="90ba6930ebb4514445ac5a7659a26948")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-mkdescr", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-arrangements", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-exactranktests", type=("build", "run"))
	depends_on("r-miceadds", type=("build", "run"))
