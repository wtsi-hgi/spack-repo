# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRaex10stprobesetDb(RPackage):
	"""Affymetrix raex10 annotation data (chip raex10stprobeset)

	Affymetrix raex10 annotation data (chip raex10stprobeset) assembled using data from public repositories
	"""
	
	bioc = "raex10stprobeset.db" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/raex10stprobeset.db_8.8.0.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/raex10stprobeset.db/raex10stprobeset.db_8.8.0.tar.gz"]

	version("8.8.0", md5="a386809ea8da340f315e378fa329b3ac")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-rn-eg-db@3.13:", type=("build", "run"))

	# annotation