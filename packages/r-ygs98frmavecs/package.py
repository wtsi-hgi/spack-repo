# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RYgs98frmavecs(RPackage):
	"""Vectors used by frma for microarrays of type ygs98

	This package was created by frmaTools version 1.19.3 and hgu133ahsentrezgcdf version 19.0.0.
	"""
	
	bioc = "ygs98frmavecs" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/ygs98frmavecs_1.3.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/ygs98frmavecs/ygs98frmavecs_1.3.0.tar.gz"]

	version("1.3.0", sha256="35b95fd91f00b3a1e22a9d342fc22fe1f755810a6fdbd3d4e676da9e800835f7")

	depends_on("r@2.10:", type=("build", "run"))

