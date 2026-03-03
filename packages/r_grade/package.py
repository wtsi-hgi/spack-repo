# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGrade(RPackage):
	"""Binary Grading functions for R

	Provides functions for matching student-answers to teacher answers for a variety of data types.
	"""
	
	homepage = "https://github.com/ltjohnson/grade"
	cran = "grade" 

	version("0.2-1", md5="3e83de031cc357003900abd6922d587c")

	depends_on("r@2.4.1:", type=("build", "run"))
