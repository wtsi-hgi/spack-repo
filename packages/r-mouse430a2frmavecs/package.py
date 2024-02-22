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
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/mouse430a2frmavecs_1.3.0.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/mouse430a2frmavecs/mouse430a2frmavecs_1.3.0.tar.gz"]

	version("1.3.0", md5="3bcb8de9182bbb8de5d560748eafa0cc")

	depends_on("r@2.10:", type=("build", "run"))

	# annotation