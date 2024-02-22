# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBiogeom(RPackage):
	"""Biological Geometries

	Is used to simulate and fit biological geometries. 'biogeom' incorporates several novel universal parametric equations that can generate the profiles of bird eggs, flowers, linear and lanceolate leaves, seeds, starfish, and tree-rings (Gielis (2003) <doi:10.3732/ajb.90.3.333>; Shi et al. (2020) <doi:10.3390/sym12040645>), three growth-rate curves representing the ontogenetic growth trajectories of animals and plants against time, and the axially symmetrical and integral forms of all these functions (Shi et al. (2017) <doi:10.1016/j.ecolmodel.2017.01.012>; Shi et al. (2021) <doi:10.3390/sym13081524>). The optimization method proposed by Nelder and Mead (1965) <doi:10.1093/comjnl/7.4.308> was used to estimate model parameters. 'biogeom' includes several real data sets of the boundary coordinates of natural shapes, including avian eggs, fruit, lanceolate and ovate leaves, tree rings, seeds, and sea stars,and can be potentially applied to other natural shapes. 'biogeom' can quantify the conspecific or interspecific similarity of natural outlines, and provides information with important ecological and evolutionary implications for the growth and form of living organisms. Please see Shi et al. (2022) <doi:10.1111/nyas.14862> for details.
	"""
	
	cran = "biogeom" 

	version("1.4.1", md5="b841226d467c7554ae6e11a19a3e8f8e")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-spatstat-geom@2.4.0:", type=("build", "run"))
