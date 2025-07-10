# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHu35ksubacdf(RPackage):
	"""hu35ksubacdf

	A package containing an environment representing the Hu35KsubA.CDF file.
	"""
	
	bioc = "hu35ksubacdf" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/hu35ksubacdf_2.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/hu35ksubacdf/hu35ksubacdf_2.18.0.tar.gz"]

	version("2.18.0", sha256="01f9687569daa451226fe7a78d2d2f91eb6f07dc2b7a5218a820a774ad0a84ab")

	depends_on("r-annotationdbi", type=("build", "run"))

