# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPagemap(RPackage):
	"""Create Mini Map for Web Pages

	Quickly and easily add a mini map to your 'rmarkdown' html documents.
	"""
	
	homepage = "https://github.com/swsoyee/pagemapR"
	cran = "pagemap" 

	version("0.1.3", md5="58bbd0532b4c27d97c9aa8eddacdf603")

	depends_on("r-htmlwidgets", type=("build", "run"))
