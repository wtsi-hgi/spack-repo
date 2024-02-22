# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIlluminamousev1p1Db(RPackage):
	"""Illumina MouseWG6v1p1 annotation data (chip illuminaMousev1p1)

	Illumina MouseWG6v1p1 annotation data (chip illuminaMousev1p1) assembled using data from public repositories
	"""
	
	bioc = "illuminaMousev1p1.db" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/illuminaMousev1p1.db_1.26.0.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/illuminaMousev1p1.db/illuminaMousev1p1.db_1.26.0.tar.gz"]

	version("1.26.0", md5="f6a4af01480a6f8d1d2d9b9b64a2b073")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-mm-eg-db@3.1.2:", type=("build", "run"))

	# annotation