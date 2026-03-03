# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROews2020(RPackage):
	"""May 2020 Occupational Employment and Wage Statistics

	Contains data from the May 2020 Occupational Employment and 
    Wage Statistics data release from the U.S. Bureau of Labor Statistics. The 
    dataset covers employment and wages across occupations, industries, states,  
    and at the national level. Metropolitan data is not included.
	"""
	
	cran = "oews2020" 

	version("1.0.0", md5="5599258100dd58b7352af2be84ab77d1", url="https://cran.r-project.org/src/contrib/oews2020_1.0.0.tar.gz")

	depends_on("r@3.5:", type=("build", "run"))
