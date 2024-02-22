# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRawsProfile(RPackage):
	"""Managing Profiles on Amazon Web Service

	This is an R wrapper from the AWS Command Line Interface that 
  provides methods to manage the user configuration on Amazon Web Service. You 
  can create as many profiles as you want, manage them, and delete them. The 
  profiles created with this tool work with all AWS products such as S3, 
  Glacier, and EC2. It also provides a function to automatically install 
  AWS CLI, but you can download it and install it manually if you prefer.
	"""
	
	cran = "raws.profile" 

	version("0.1.0", md5="e2d1fab4875a66abef5b91f2d78e7f49")

	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
