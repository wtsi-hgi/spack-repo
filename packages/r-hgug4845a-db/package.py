# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHgug4845aDb(RPackage):
	"""agilent AMADID 026652 annotation data (chip hgug4845a)

	agilent AMADID 026652 annotation data (chip hgug4845a) assembled using data from public repositories
	"""
	
	bioc = "hgug4845a.db" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/hgug4845a.db_0.0.3.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/hgug4845a.db/hgug4845a.db_0.0.3.tar.gz"]

	version("0.0.3", sha256="464f1ea84aa09ec922dbfbe6050fc88e4ba68cba8be2e0ba05c44f6facb063a4")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-hs-eg-db@2.7.1:", type=("build", "run"))

