# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCelltrackr(RPackage):
	"""Motion Trajectory Analysis

	Methods for analyzing (cell) motion in two or three dimensions.
	Available measures include displacement, confinement ratio, autocorrelation,
	straightness, turning angle, and fractal dimension. Measures can be applied to entire tracks,
	steps, or subtracks with varying length. While the methodology has been developed for
	cell trajectory analysis, it is applicable to anything that moves including animals,
	people, or vehicles.
	Some of the methodology implemented in this packages was described by: 
	Beauchemin, Dixit, and Perelson (2007) <doi:10.4049/jimmunol.178.9.5505>, 
	Beltman, Maree, and de Boer (2009) <doi:10.1038/nri2638>,
	Gneiting and Schlather (2004) <doi:10.1137/S0036144501394387>,
	Mokhtari, Mech, Zitzmann, Hasenberg, Gunzer, and Figge (2013) <doi:10.1371/journal.pone.0080808>,
	Moreau, Lemaitre, Terriac, Azar, Piel, Lennon-Dumenil, and Bousso (2012) <doi:10.1016/j.immuni.2012.05.014>,
	Textor, Peixoto, Henrickson, Sinn, von Andrian, and Westermann (2011) <doi:10.1073/pnas.1102288108>,
  Textor, Sinn, and de Boer (2013) <doi:10.1186/1471-2105-14-S6-S10>,
  Textor, Henrickson, Mandl, von Andrian, Westermann, de Boer, and Beltman (2014) <doi:10.1371/journal.pcbi.1003752>.
	"""
	
	homepage = "http://www.motilitylab.net"
	cran = "celltrackR" 

	version("1.2.0", md5="a250cf77c93bf3a632ba1a09451833b4")
	version("1.1.0", md5="6109e8f8a7702ba65a8d8fd0dd1cb7d4")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ellipse", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
