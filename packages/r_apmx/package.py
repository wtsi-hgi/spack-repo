# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RApmx(RPackage):
	"""Automated Population Pharmacokinetic Dataset Assembly

	Automated methods to assemble population PK (pharmacokinetic) and
    PKPD (pharmacodynamic) datasets for analysis in 'NONMEM' (non-linear mixed effects
    modeling) by Bauer (2019) <doi:10.1002/psp4.12404>. The package includes functions
    to build datasets from SDTM (study data tabulation module)
    <https://www.cdisc.org/standards/foundational/sdtm>, ADaM (analysis dataset
    module) <https://www.cdisc.org/standards/foundational/adam>, or other dataset
    formats. The package will combine population datasets, add covariates, and
    create documentation to support regulatory submission and internal communication.
	"""
	
	homepage = "https://github.com/stephen-amori/apmx"
	cran = "apmx" 

	version("1.1.1", md5="257aa3adab73a563a6381cc4a3f725d0")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-this-path", type=("build", "run"))
	depends_on("r-flextable", type=("build", "run"))
	depends_on("r-officer", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-arsenal", type=("build", "run"))
