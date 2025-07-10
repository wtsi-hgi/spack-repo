# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHs25kresogenDb(RPackage):
	"""RNG_MRC Human Pangenomic 25k Set annotation data (chip hs25kresogen)

	RNG_MRC Human Pangenomic 25k Set annotation data (chip hs25kresogen) assembled using data from public repositories
	"""
	
	bioc = "hs25kresogen.db" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/hs25kresogen.db_2.5.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/hs25kresogen.db/hs25kresogen.db_2.5.0.tar.gz"]

	version("2.5.0", sha256="ce37eb65761aa00fe07b05d60d733bd146aa0befb4c68dea9f9faf515d2ce2fa")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-hs-eg-db@2.5:", type=("build", "run"))

