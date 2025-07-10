# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHtratfocusDb(RPackage):
	"""Affymetrix Affymetrix HT_Rat-Focus Array annotation data (chip htratfocus)

	Affymetrix Affymetrix HT_Rat-Focus Array annotation data (chip htratfocus) assembled using data from public repositories
	"""
	
	bioc = "htratfocus.db" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/htratfocus.db_3.13.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/htratfocus.db/htratfocus.db_3.13.0.tar.gz"]

	version("3.13.0", sha256="e9e421ea6c53342f64ad04a76615e2f30bee570f700f7934bc0fb79a6e73f82c")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-rn-eg-db@3.13:", type=("build", "run"))

