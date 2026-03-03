# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPublicCtn0094extra(RPackage):
	"""Helper Files for the CTN-0094 Relational Database

	Engineered features and "helper" functions ancillary to the
    'public.ctn0094data' package, extending this package for ease of use (see 
    <https://CRAN.R-project.org/package=public.ctn0094data>). This
    'public.ctn0094data' package contains harmonized datasets from some of the
    National Institute of Drug Abuse's Clinical Trials Network (NIDA's CTN)
    projects. Specifically, the CTN-0094 project is to harmonize and de-identify
    clinical trials data from the CTN-0027, CTN-0030, and CTN-51 studies for
    opioid use disorder. This current version is built from 'public.ctn0094data'
    v. 1.0.6.
	"""
	
	homepage = "https://ctn-0094.github.io/public.ctn0094extra/"
	cran = "public.ctn0094extra" 

	version("1.0.4", md5="ab269b214e97c94c14edc26157a9ee6b")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-public-ctn0094data", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
