# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShorts(RPackage):
	"""Short Sprints

	Create short sprint acceleration-velocity (AVP) and force-velocity (FVP) profiles
     and predict kinematic and kinetic variables using the timing-gate split times, laser or 
     radar gun data, tether devices data, as well as the data provided by the GPS and LPS 
     monitoring systems. The modeling method utilized in this package is based on the works of 
    Furusawa K, Hill AV, Parkinson JL (1927) <doi: 10.1098/rspb.1927.0035>, 
    Greene PR. (1986) <doi: 10.1016/0025-5564(86)90063-5>, 
    Chelly SM, Denis C. (2001) <doi: 10.1097/00005768-200102000-00024>,
    Clark KP, Rieger RH, Bruno RF, Stearne DJ. (2017) <doi: 10.1519/JSC.0000000000002081>, 
    Samozino P. (2018) <doi: 10.1007/978-3-319-05633-3_11>, 
    Samozino P. and Peyrot N., et al (2022) <doi: 10.1111/sms.14097>, 
    Clavel, P., et al (2023) <doi: 10.1016/j.jbiomech.2023.111602>, and 
    Jovanovic M. (2023) <doi: 10.1080/10255842.2023.2170713>.
	"""
	
	homepage = "https://mladenjovanovic.github.io/shorts/"
	cran = "shorts" 

	version("3.1.0", md5="33875c34683eecc30ca96b4abcc642be")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-lambertw", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-minpack-lm", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
