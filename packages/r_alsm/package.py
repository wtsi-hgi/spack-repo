# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAlsm(RPackage):
	"""Companion to Applied Linear Statistical Models

	Functions and Data set presented in Applied Linear Statistical Models Fifth Edition (Chapters 1-9 and 16-25), Michael H. Kutner; Christopher J. Nachtsheim; John Neter; William Li, 2005. (ISBN-10: 0071122214, ISBN-13: 978-0071122214) that do not exist in R, are gathered in this package. The whole book will be covered in the next versions.
	"""
	
	cran = "ALSM" 

	version("0.2.0", md5="d5d6f5420165b9326b629e26b8185f07")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-leaps", type=("build", "run"))
	depends_on("r-suppdists", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
