# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMouse4302frmavecs(RPackage):
	"""Vectors used by frma for microarrays of type mouse4302

	This package was created by frmaTools version 1.19.3 and hgu133ahsentrezgcdf version 19.0.0.
	"""
	
	bioc = "mouse4302frmavecs" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/mouse4302frmavecs_1.5.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/mouse4302frmavecs/mouse4302frmavecs_1.5.0.tar.gz"]

	version("1.5.0", sha256="fa5c298b441c5a8c0f49983013b7e100910d879a73ab856de618bff0dde49411")

	depends_on("r@2.10:", type=("build", "run"))

