# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMgug4104aDb(RPackage):
	"""Agilent annotation data (chip mgug4104a)

	Agilent annotation data (chip mgug4104a) assembled using data from public repositories
	"""
	
	bioc = "mgug4104a.db" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/mgug4104a.db_3.2.3.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/mgug4104a.db/mgug4104a.db_3.2.3.tar.gz"]

	version("3.2.3", md5="7b1cef094a226257cd657ed8d61e9ef1")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-mm-eg-db@3.3:", type=("build", "run"))

	# annotation