# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIineq(RPackage):
	"""Computing Individual Components of the Gini and the Theil
Indices

	Computes individual contributions to the overall Gini and 
    Theil's T and Theil's L measures and their decompositions by groups 
    such as race, gender, national origin, with the three functions of 
    iGini(), iTheiT(), and iTheilL(). For details, see Tim F. Liao (2019)
    <doi:10.1177/0049124119875961>.
	"""
	
	cran = "iIneq" 

	version("1.0.2", md5="4167a4eab96d5bf63b14bd86f0c85d04")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-foreach@1.4.8:", type=("build", "run"))
	depends_on("r-doparallel@1.0.15:", type=("build", "run"))
