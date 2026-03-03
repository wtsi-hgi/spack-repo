# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVoteogram(RPackage):
	"""United States House and Senate Voting Cartogram Generators

	'ProPublica' <https://projects.propublica.org/represent/> makes United States
    Congress member votes available and has developed their own unique cartogram to visually
    represent this data. Tools are provided to retrieve voting data, prepare voting data 
    for plotting with 'ggplot2', create vote cartograms and theme them.
	"""
	
	homepage = "https://github.com/hrbrmstr/voteogram"
	cran = "voteogram" 

	version("0.3.2", md5="4a6e920ed1ebd05fd8789dee08a1cde7")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-ggplot2@3.4.1:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
