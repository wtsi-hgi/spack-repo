# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHu35ksubccdf(RPackage):
	"""hu35ksubccdf

	A package containing an environment representing the Hu35KsubC.CDF file.
	"""
	
	bioc = "hu35ksubccdf" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/hu35ksubccdf_2.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/hu35ksubccdf/hu35ksubccdf_2.18.0.tar.gz"]

	version("2.18.0", sha256="f15a047c6912c5c196389c06e8aa4ddc81781e49856f043128923dab0f57cc3b")

	depends_on("r-annotationdbi", type=("build", "run"))

