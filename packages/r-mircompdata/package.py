# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMircompdata(RPackage):
	"""Data used in the miRcomp package

	Raw amplification data from a large microRNA mixture / dilution study. These data are used by the miRcomp package to assess the performance of methods that estimate expression from the amplification curves.
	"""
	
	bioc = "miRcompData" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/miRcompData_1.32.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/miRcompData/miRcompData_1.32.0.tar.gz"]

	version("1.32.0", sha256="e61d11cd0352745d221517f0f85654ad6e5923d2670eeff0069797db1bdd8897")

	depends_on("r@3.2:", type=("build", "run"))

