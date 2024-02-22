# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDsjobtracker(RPackage):
	"""What Skills and Qualifications are Required for Data Science
Related Jobs?

	Dataset containing information about job listings for data science job roles.
	"""
	
	homepage = "https://github.com/thiyangt/DSjobtracker"
	cran = "DSjobtracker" 

	version("2.0.0", md5="d0c0c1ff454b23988dcaac6932781555")

	depends_on("r@3.5:", type=("build", "run"))
