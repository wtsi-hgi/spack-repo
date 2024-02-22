# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBeezdiscounting(RPackage):
	"""Behavioral Economic Easy Discounting

	Facilitates some of the analyses performed in studies of
    behavioral economic discounting. The package supports scoring of the 27-Item Monetary Choice
    Questionnaire (see Kaplan et al., 2016; <doi:10.1007/s40614-016-0070-9>) and scoring of the 
    minute discounting task (see Koffarnus & Bickel, 2014; <doi:10.1037/a0035973>) using the 
    Qualtrics 5-trial discounting template (see the Qualtrics Minute Discounting User Guide; 
    <doi:10.13140/RG.2.2.26495.79527>), which is also available as a .qsf file in this package. 
	"""
	
	homepage = "https://github.com/brentkaplan/beezdiscounting"
	cran = "beezdiscounting" 

	version("0.3.1", md5="37a0e3296207418116481f4d0b37e8d9")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-psych", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
