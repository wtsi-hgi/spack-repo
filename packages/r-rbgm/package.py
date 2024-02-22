# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRbgm(RPackage):
	"""Tools for 'Box Geometry Model' (BGM) Files and Topology for the
Atlantis Ecosystem Model

	Facilities for working with Atlantis box-geometry model (BGM) 
 files. Atlantis is a deterministic, biogeochemical, whole-of-ecosystem model. 
 Functions are provided to read from BGM files directly, preserving their 
 internal topology, as well as helper functions to generate spatial data from these
 mesh forms. This functionality aims to simplify the creation and modification of box 
 and geometry as well as the ability to integrate with other data sources. 
	"""
	
	homepage = "https://research.csiro.au/atlantis/"
	cran = "rbgm" 

	version("0.1.0", md5="5628e0821206c81dd27ef92d5192d608")

	depends_on("r@3.2.2:", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-geosphere", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-reproj", type=("build", "run"))
	depends_on("r-sfheaders", type=("build", "run"))
