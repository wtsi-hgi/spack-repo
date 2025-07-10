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
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/raex10stprobeset.db_8.8.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/raex10stprobeset.db/raex10stprobeset.db_8.8.0.tar.gz"]

	version("8.8.0", sha256="c35dfccc3164bc87a24410fc43cb0e0fa16c28a65e91c47db83ad8b762911865")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-rn-eg-db@3.13:", type=("build", "run"))

