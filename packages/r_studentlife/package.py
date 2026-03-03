# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStudentlife(RPackage):
	"""Tidy Handling and Navigation of the Student-Life Dataset

	Download, navigate and analyse the Student-Life dataset. 
    The Student-Life dataset contains passive and automatic sensing data 
    from the phones of a class of 48 Dartmouth college students. 
    It was collected over a 10 week term. Additionally, the dataset contains ecological 
    momentary assessment results along with pre-study and post-study mental  
    health surveys. The intended use is to assess 
    mental health, academic performance and behavioral trends. 
    The raw dataset and additional information is 
    available at <https://studentlife.cs.dartmouth.edu/>.
	"""
	
	homepage = "https://github.com/Frycast/studentlife"
	cran = "studentlife" 

	version("1.1.0", md5="4268968f183f4b82ea9ad9973655b696")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-purrr@0.3.2:", type=("build", "run"))
	depends_on("r-readr@1.3.1:", type=("build", "run"))
	depends_on("r-tidyr@0.8.3:", type=("build", "run"))
	depends_on("r-dplyr@0.8.0.1:", type=("build", "run"))
	depends_on("r-jsonlite@1.6:", type=("build", "run"))
	depends_on("r-tibble@2.0.1:", type=("build", "run"))
	depends_on("r-r-utils@2.8:", type=("build", "run"))
	depends_on("r-skimr@1.0.7:", type=("build", "run"))
	depends_on("r-visdat@0.5.3:", type=("build", "run"))
	depends_on("r-ggplot2@3.1.1:", type=("build", "run"))
	depends_on("r-crayon@1.3.4:", type=("build", "run"))
