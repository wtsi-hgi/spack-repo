# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RReproj(RPackage):
	"""Coordinate System Transformations for Generic Map Data

	Transform coordinates from a specified source to a specified 
 target map projection. This uses the 'PROJ' library directly, by wrapping the 
 'PROJ' package which leverages 'libproj', otherwise the 'proj4' package. The 'reproj()' 
 function is generic, methods may be added to remove the need for an explicit 
 source definition. If 'proj4' is in use 'reproj()' handles the requirement for 
 conversion of angular units where necessary. This is for use primarily to 
 transform generic data formats and direct leverage of the underlying
 'PROJ' library. (There are transformations that aren't possible with 'PROJ' and
 that are provided by the 'GDAL' library, a limitation which users of this 
 package should be aware of.) The 'PROJ' library is available at 
 <https://proj.org/>.  
	"""
	
	homepage = "https://github.com/hypertidy/reproj/"
	cran = "reproj" 

	version("0.4.3", md5="08cada68192263a2087ca7bcc3d30e35")

	depends_on("r@3.2.5:", type=("build", "run"))
	depends_on("r-proj4", type=("build", "run"))
	depends_on("r-proj@0.4:", type=("build", "run"))
	depends_on("r-crsmeta@0.3:", type=("build", "run"))
	depends_on("proj@4.4.6:", type=("build", "link", "run"))
