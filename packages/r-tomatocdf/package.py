# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTomatocdf(RPackage):
	"""tomatocdf

	A package containing an environment representing the Tomato.cdf file.
	"""
	
	bioc = "tomatocdf" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/tomatocdf_2.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/tomatocdf/tomatocdf_2.18.0.tar.gz"]

	version("2.18.0", sha256="d5c6b83ee59f71b1855b9427ffd71f5d74588a8f6a58b86cd1750bf8fb2db8d1")

	depends_on("r-annotationdbi", type=("build", "run"))

