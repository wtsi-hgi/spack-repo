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

	version("2.18.0", md5="ed6e86398e51c7b0ddca4431797ecbc0")

	depends_on("r-annotationdbi", type=("build", "run"))

