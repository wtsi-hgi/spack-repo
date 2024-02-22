# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJmvreadwrite(RPackage):
	"""Read and Write 'jamovi' Files ('.omv')

	The free and open a statistical spreadsheet 'jamovi'
    (<https://www.jamovi.org>) aims to make statistical analyses easy and
    intuitive. 'jamovi' produces syntax that can directly be used in R (in
    connection with the R-package 'jmv'). Having import / export routines for
    the data files 'jamovi' produces ('.omv') permits an easy transfer of
    data and analyses between 'jamovi' and R.
	"""
	
	homepage = "https://sjentsch.github.io/jmvReadWrite/"
	cran = "jmvReadWrite" 

	version("0.4.2", md5="e931d015d6e5e6112e031cf22a29e09b")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-zip", type=("build", "run"))
