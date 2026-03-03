# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBumblebee(RPackage):
	"""Quantify Disease Transmission Within and Between Population
Groups

	A simple tool to quantify the amount of transmission
   of an infectious disease of interest occurring within and between 
   population groups. 'bumblebee' uses counts of observed directed 
   transmission pairs, identified phylogenetically from deep-sequence data or 
   from epidemiological contacts, to quantify transmission flows within and 
   between population groups accounting for sampling heterogeneity. Population 
   groups might include: geographical areas (e.g. communities, regions), 
   demographic groups (e.g. age, gender) or arms of a randomized clinical 
   trial. See the 'bumblebee' website for statistical theory, documentation 
   and examples <https://magosil86.github.io/bumblebee/>.
	"""
	
	homepage = "https://magosil86.github.io/bumblebee/"
	cran = "bumblebee" 

	version("0.1.0", md5="0f1cd45446001aae3c6f520100588775")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr@1.0.2:", type=("build", "run"))
	depends_on("r-gtools@3.8.2:", type=("build", "run"))
	depends_on("r-hmisc@4.4.2:", type=("build", "run"))
	depends_on("r-magrittr@2.0.1:", type=("build", "run"))
	depends_on("r-rmarkdown@2.6:", type=("build", "run"))
