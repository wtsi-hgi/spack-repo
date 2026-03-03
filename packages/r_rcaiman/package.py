# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcaiman(RPackage):
	"""CAnopy IMage ANalysis

	Classify hemispherical 
    photographs of the plant canopy with algorithms specially developed for 
    such a task and well documented in 
    Díaz and Lencinas (2015) <doi:10.1109/lgrs.2015.2425931> and 
    Díaz and Lencinas (2018) <doi:10.1139/cjfr-2018-0006>. It supports 
    non-circular hemispherical photography, such as those acquired with  
    15mm lenses or with auxiliary fish-eye lenses attached to mobile devices. 
    For smartphone-based hemispherical photography see 
    Díaz (2023) <doi:10.1111/2041-210x.14059>. Most of the functions also 
    support restricted view photography.
	"""
	
	cran = "rcaiman" 

	version("1.2.2", md5="8f3328be3423a2e4611795c9f7286953")

	depends_on("r-filenamer", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-colorspace", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
	depends_on("r-testthat", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-spatial", type=("build", "run"))
	depends_on("r-lidr", type=("build", "run"))
