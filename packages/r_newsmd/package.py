# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNewsmd(RPackage):
	"""Creation of NEWS.md File

	Adding updates (version or bullet points) to the NEWS.md
    file.
	"""
	
	homepage = "https://github.com/Dschaykib/newsmd"
	cran = "newsmd" 

	version("0.5.1", md5="b21b658b462af045c8bdc87b4c9f84be")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
