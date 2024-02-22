# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHgu133plus2frmavecs(RPackage):
	"""Vectors used by frma for microarrays of type hgu133plus2

	This package was created by frmaTools version 1.19.3 and hgu133ahsentrezgcdf version 19.0.0.
	"""
	
	bioc = "hgu133plus2frmavecs" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/hgu133plus2frmavecs_1.5.0.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/hgu133plus2frmavecs/hgu133plus2frmavecs_1.5.0.tar.gz"]

	version("1.5.0", md5="a4781cbcccc1ee17dfd16259f1c7bebc")

	depends_on("r@2.10:", type=("build", "run"))

	# annotation