# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSparkhail(RPackage):
	"""A 'Sparklyr' Extension for 'Hail'

	'Hail' is an open-source, general-purpose, 'python' based data analysis
    tool with additional data types and methods for working with genomic data, see
    <https://hail.is/>. 'Hail' is built to scale and has first-class support for 
    multi-dimensional structured data, like the genomic data in a genome-wide 
    association study (GWAS). 'Hail' is exposed as a 'python' library, using primitives
    for distributed queries and linear algebra implemented in 'scala', 'spark', and 
    increasingly 'C++'. The 'sparkhail' is an R extension using 'sparklyr' package. 
    The idea is to help R users to use 'hail' functionalities with the well-know
    'tidyverse' syntax, see <https://www.tidyverse.org/>.
	"""
	
	cran = "sparkhail" 

	version("0.1.1", md5="cfc3df0c3357e81d1b3a5cb145258fd2")

	depends_on("r@3.1.2:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-sparklyr@1.0.1:", type=("build", "run"))
	depends_on("r-sparklyr-nested", type=("build", "run"))
