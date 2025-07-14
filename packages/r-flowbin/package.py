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

	version("1.44.0", commit="49acac2105f788495d5a53faed41ba1ed5143351")
	version("1.38.0", commit="2b7343da3d603e3f45cc3c6dab81b25c737769fe")

	depends_on("r-flowcore", type=("build", "run"))
	depends_on("r-flowfp", type=("build", "run"))
	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-class", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-snow", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
