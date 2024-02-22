# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RModacdc(RPackage):
	"""Association of Covariance for Detecting Differential
Co-Expression

	A series of functions to implement association of covariance for detecting differential co-expression (ACDC), a novel approach for detection of differential co-expression that simultaneously accommodates multiple phenotypes or exposures with binary, ordinal, or continuous data types. Users can use the default method which identifies modules by Partition or may supply their own modules. Also included are functions to choose an information loss criterion (ILC) for Partition using OmicS-data-based Complex trait Analysis (OSCA) and Genome-wide Complex trait Analysis (GCTA). The manuscript describing these methods is as follows: Queen K, Nguyen MN, Gilliland F, Chun S, Raby BA, Millstein J. "ACDC: a general approach for detecting phenotype or exposure associated co-expression" (2023) <doi:10.3389/fmed.2023.1118824>.
	"""
	
	homepage = "https://github.com/USCbiostats/ACDC"
	cran = "modACDC" 

	version("2.0.1", md5="1e5155316d35a62c28fe15897bdc98e1")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-ccp", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-genieclust", type=("build", "run"))
	depends_on("r-genio", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-partition", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
