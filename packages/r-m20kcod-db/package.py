# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RM20kcodDb(RPackage):
	"""Codelink UniSet Mouse 20k I Bioarray annotation data (chip m20kcod)

	Codelink UniSet Mouse 20k I Bioarray annotation data (chip m20kcod) assembled using data from public repositories
	"""
	
	bioc = "m20kcod.db" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/m20kcod.db_3.4.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/m20kcod.db/m20kcod.db_3.4.0.tar.gz"]

	version("3.4.0", sha256="d7061fc9ef1b4248fbae681d5abd7170307260c604a5c5f8c711944564a95adc")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-mm-eg-db@3.2.1:", type=("build", "run"))

