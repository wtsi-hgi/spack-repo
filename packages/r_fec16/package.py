# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFec16(RPackage):
	"""Data Package for the 2016 United States Federal Elections

	Easily analyze relational data from the United States 2016 federal 
    election cycle as reported by the Federal Election Commission.
    This package contains data about candidates, committees, and a
    variety of different financial expenditures. Data is from <https://www.fec.gov/data/browse-data/?tab=bulk-data>. 
	"""
	
	homepage = "https://github.com/baumer-lab/fec16"
	cran = "fec16" 

	version("0.1.4", md5="02479cdadd3f02963bbd8ed8597adc51", url="https://cran.r-project.org/src/contrib/fec16_0.1.4.tar.gz")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-vroom", type=("build", "run"))
	depends_on("r-usethis", type=("build", "run"))
