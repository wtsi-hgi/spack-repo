# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RE4tools(RPackage):
	"""Management and Processing Tools for Data Produced by the
Empatica E4

	Process and manage the data from the Empatica E4. All functions operate on the EDA data stream, but other streams will be added soon. The Empatica E4 is a wearable physiological monitor made by Empatica (Empatica is not associated with any of this code). You can find more information about the E4 at Empatica's website <https://www.empatica.com/research/e4/>.
	"""
	
	cran = "E4tools" 

	version("0.1.1", md5="8d4ccf389efd9be2152c355fd4ef661b")

	depends_on("r-bbmisc", type=("build", "run"))
	depends_on("r-datacombine", type=("build", "run"))
	depends_on("r-signal", type=("build", "run"))
	depends_on("r-anytime", type=("build", "run"))
	depends_on("r-chron", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-accelerometry", type=("build", "run"))
	depends_on("r-hms", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-dosnow", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
