# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDoolkit(RPackage):
	"""Exploration of Dental Surface Topography

	Tools for exploring the topography of 3d triangle meshes.
    The functions were developed with dental surfaces in mind, but could be 
    applied to any triangle mesh of class 'mesh3d'. More specifically, 'doolkit'
    allows to isolate the border of a mesh, or a subpart of the mesh using the 
    polygon networks method; crop a mesh; compute basic descriptors (elevation, 
    orientation, footprint area); compute slope, angularity and relief index
    (Ungar and Williamson (2000) <https://palaeo-electronica.org/2000_1/gorilla/issue1_00.htm>;
    Boyer (2008) <doi:10.1016/j.jhevol.2008.08.002>), inclination and occlusal
    relief index or gamma (Guy et al. (2013) <doi:10.1371/journal.pone.0066142>),
    OPC (Evans et al. (2007) <doi:10.1038/nature05433>), OPCR (Wilson et al. 
    (2012) <doi:10.1038/nature10880>), DNE (Bunn et al. (2011) <doi:10.1002/ajpa.21489>;
    Pampush et al. (2016) <doi:10.1007/s10914-016-9326-0>), form factor (Horton 
    (1932) <doi:10.1029/TR013i001p00350>), basin elongation (Schum (1956) 
    <doi:10.1130/0016-7606(1956)67[597:EODSAS]2.0.CO;2>), lemniscate ratio 
    (Chorley et al; (1957) <doi:10.2475/ajs.255.2.138>), enamel-dentine distance
    (Guy et al. (2015) <doi:10.1371/journal.pone.0138802>; Thiery et al. (2017) 
    <doi:10.3389/fphys.2017.00524>), absolute crown strength (Schwartz et al. 
    (2020) <doi:10.1098/rsbl.2019.0671>), relief rate (Thiery et al. (2019)
    <doi:10.1002/ajpa.23916>) and area-relative curvature; draw cumulative
    profiles of a topographic variable; and map a variable over a 3d triangle 
    mesh.
	"""
	
	cran = "doolkit" 

	version("1.42.2", md5="d92e4ffc670f76f9c080281deeda50c3")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-morpho", type=("build", "run"))
	depends_on("r-rgl", type=("build", "run"))
	depends_on("r-rvcg", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-tis", type=("build", "run"))
	depends_on("r-concaveman", type=("build", "run"))
	depends_on("r-usethis", type=("build", "run"))
