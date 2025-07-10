# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMgu74acdf(RPackage):
	"""mgu74acdf

	A package containing an environment representing the MG_U74A.cdf file.
	"""
	
	bioc = "mgu74acdf" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/mgu74acdf_2.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/mgu74acdf/mgu74acdf_2.18.0.tar.gz"]

	version("2.18.0", sha256="8ffa617103860c4ab5a72304eb42523a2010e6ac0f24008d48dc5bdb8247f3a0")

	depends_on("r-annotationdbi", type=("build", "run"))

