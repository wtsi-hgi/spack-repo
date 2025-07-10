# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMouse430a2frmavecs(RPackage):
	"""Vectors used by frma for microarrays of type mouse430a2

	This package was created by frmaTools version 1.19.3 and hgu133ahsentrezgcdf version 19.0.0.
	"""
	
	bioc = "mouse430a2frmavecs" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/mouse430a2frmavecs_1.3.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/mouse430a2frmavecs/mouse430a2frmavecs_1.3.0.tar.gz"]

	version("1.3.0", sha256="08da8517645125999e6c0f3d76b1aff45c6eee0d76ae9a784387cf493e76692d")

	depends_on("r@2.10:", type=("build", "run"))

