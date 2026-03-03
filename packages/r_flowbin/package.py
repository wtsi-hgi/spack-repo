# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFlowbin(RPackage):
	"""Combining multitube flow cytometry data by binning

	Software to combine flow cytometry data that has been multiplexed into multiple tubes with common markers between them, by establishing common bins across tubes in terms of the common markers, then determining expression within each tube for each bin in terms of the tube-specific markers.
	"""
	
	bioc = "flowBin" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/flowBin_1.38.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/flowBin/flowBin_1.38.0.tar.gz"]

	version("1.38.0", md5="3d761d597ff6b4f6929e9f68ea83b366")

	depends_on("r-flowcore", type=("build", "run"))
	depends_on("r-flowfp", type=("build", "run"))
	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-class", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-snow", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
