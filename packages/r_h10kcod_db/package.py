# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RH10kcodDb(RPackage):
	"""Codelink UniSet Human I Bioarray (~10 000 human genes) annotation data (chip h10kcod)

	Codelink UniSet Human I Bioarray (~10 000 human genes) annotation data (chip h10kcod) assembled using data from public repositories
	"""
	
	bioc = "h10kcod.db" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/h10kcod.db_3.4.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/h10kcod.db/h10kcod.db_3.4.0.tar.gz"]

	version("3.4.0", md5="a555739cea229f286953c3297c145e9c")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-hs-eg-db@3.2.1:", type=("build", "run"))

