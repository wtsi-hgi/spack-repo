# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTapes(RPackage):
	"""Tree Taper Curves and Sorting Based on 'TapeR'

	Providing new german-wide 'TapeR' Models and functions for their 
  evaluation. Included are the most common tree species in Germany (Norway 
  spruce, Scots pine, European larch, Douglas fir, Silver fir as well as 
  European beech, Common/Sessile oak and Red oak). Many other species are mapped
  to them so that 36 tree species / groups can be processed. Single trees are 
  defined by species code, one or multiple diameters in arbitrary measuring 
  height and tree height. The functions then provide information on diameters 
  along the stem, bark thickness, height of diameters, volume of the total or 
  parts of the trunk and total and component above-ground biomass. It is also 
  possible to calculate assortments from the taper curves. For diameter and 
  volume estimation, uncertainty information is given.
	"""
	
	homepage = "https://gitlab.com/vochr/tapes"
	cran = "TapeS" 

	version("0.12.1", md5="520f56c03f9035a0aaf828c6386935f5")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-taper@0.5.2:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
