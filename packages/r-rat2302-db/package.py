# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRat2302Db(RPackage):
	"""Affymetrix Affymetrix Rat230_2 Array annotation data (chip rat2302)

	Affymetrix Affymetrix Rat230_2 Array annotation data (chip rat2302) assembled using data from public repositories
	"""
	
	bioc = "rat2302.db" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/rat2302.db_3.13.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/rat2302.db/rat2302.db_3.13.0.tar.gz"]

	version("3.13.0", sha256="0c0f92ebc4aac924a12e512caddb57226286494ec2d8514591b30f7c73a858cc")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-rn-eg-db@3.13:", type=("build", "run"))

