# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSleuth3(RPackage):
	"""Data Sets from Ramsey and Schafer's "Statistical Sleuth (3rd
Ed)"

	Data sets from Ramsey, F.L. and Schafer, D.W. (2013), "The
    Statistical Sleuth: A Course in Methods of Data Analysis (3rd
    ed)", Cengage Learning. 
	"""
	
	homepage = "https://r-forge.r-project.org/projects/sleuth2/"
	cran = "Sleuth3" 

	version("1.0-6", md5="968acccc25a9c93cfe5319a19e2413c6", url="https://cran.r-project.org/src/contrib/Sleuth3_1.0-6.tar.gz")

	depends_on("r@4.1:", type=("build", "run"))
