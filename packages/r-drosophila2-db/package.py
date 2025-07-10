# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDrosophila2Db(RPackage):
	"""Affymetrix Affymetrix Drosophila_2 Array annotation data (chip drosophila2)

	Affymetrix Affymetrix Drosophila_2 Array annotation data (chip drosophila2) assembled using data from public repositories
	"""
	
	bioc = "drosophila2.db" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/drosophila2.db_3.13.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/drosophila2.db/drosophila2.db_3.13.0.tar.gz"]

	version("3.13.0", sha256="ba71270a28d42ef47dfed60e558e28972b0b4ddaa72bd06225e8cc16a6c8960e")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-dm-eg-db@3.13:", type=("build", "run"))

