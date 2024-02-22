# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSleuth2(RPackage):
	"""Data Sets from Ramsey and Schafer's "Statistical Sleuth (2nd
Ed)"

	Data sets from Ramsey, F.L. and Schafer, D.W. (2002), "The
    Statistical Sleuth: A Course in Methods of Data Analysis (2nd
    ed)", Duxbury. 
	"""
	
	homepage = "https://r-forge.r-project.org/projects/sleuth2/"
	cran = "Sleuth2" 

	version("2.0-7", md5="deb355ef3f747735f45510d5b1d2aa18", url="https://cran.r-project.org/src/contrib/Sleuth2_2.0-7.tar.gz")

	depends_on("r@4.1:", type=("build", "run"))
