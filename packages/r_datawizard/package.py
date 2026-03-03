# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDatawizard(RPackage):
	"""Easy Data Wrangling and Statistical Transformations

	A lightweight package to assist in key steps involved in any data 
    analysis workflow: (1) wrangling the raw data to get it in the needed form, 
    (2) applying preprocessing steps and statistical transformations, and 
    (3) compute statistical summaries of data properties and distributions. 
    It is also the data wrangling backend for packages in 'easystats' ecosystem.
    References: Patil et al. (2022) <doi:10.21105/joss.04684>.
	"""
	
	homepage = "https://easystats.github.io/datawizard/"
	cran = "datawizard" 

	version("0.9.1", md5="9df4630e0cc8a06003488abde0a77137")
	version("0.10.0", md5="e40af4bc6c0a49b3696229b08a803b7e")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-insight@0.19.8:", type=("build", "run"))
