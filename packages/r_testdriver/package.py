# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTestdriver(RPackage):
	"""Teaching Data for Statistics and Data Science

	Provides data sets for teaching statistics and data science courses. 
    It includes a sample of data from John Edmund Kerrich's famous 
    coinflip experiment. These are data that I used for teaching SOC 4015 / SOC 
    5050 at Saint Louis University (SLU). The package also contains an R Markdown
    template with the required formatting for assignments in my courses 
    SOC 4015, SOC 4650, SOC 5050, and SOC 5650 at SLU.
	"""
	
	homepage = "https://github.com/chris-prener/testDriveR"
	cran = "testDriveR" 

	version("0.5.2", md5="d5ab8aa699f3bb3ff537626f54381c34")

