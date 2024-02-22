# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCtm(RPackage):
	"""A Text Mining Toolkit for Chinese Document

	The CTM package is designed to solve problems of text mining and is specific for Chinese document.
	"""
	
	cran = "CTM" 

	version("0.2", md5="99963c852b2be9aea808cce2b697e3d1")

	depends_on("r-jiebar", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
