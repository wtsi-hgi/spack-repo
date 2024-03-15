# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRgug4130aDb(RPackage):
	"""Agilent Rat annotation data (chip rgug4130a)

	Agilent Rat annotation data (chip rgug4130a) assembled using data from public repositories
	"""
	
	bioc = "rgug4130a.db" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/rgug4130a.db_3.2.3.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/rgug4130a.db/rgug4130a.db_3.2.3.tar.gz"]

	version("3.2.3", md5="13643ac109aaf12590a5b6e379609b79")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-rn-eg-db@3.3:", type=("build", "run"))

	# annotation