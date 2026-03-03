# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRgplates(RPackage):
	"""R Interface for the GPlates Web Service and Desktop Application

	Query functions to the GPlates <https://www.gplates.org/> Desktop Application and the GPlates Web Service <https://gws.gplates.org/> allow users to reconstruct past positions of geographic entities based on user-selected rotation models without leaving the R running environment. The online method (GPlates Web Service) makes the rotation of static plates, coastlines, and a low number of geographic coordinates available using nothing but an internet connection. The offline method requires an external installation of the GPlates Desktop Application, but allows the efficient batch rotation of thousands of coordinates, Simple Features (sf) and Spatial (sp) objects with custom reconstruction trees and partitioning polygons. Examples of such plate tectonic models are accessible via the chronosphere <https://cran.r-project.org/package=chronosphere>. This R extension is developed under the umbrella of the DFG (Deutsche Forschungsgemeinschaft) Research Unit TERSANE2 (For 2332, TEmperature Related Stressors in ANcient Extinctions).
	"""
	
	homepage = "https://adamtkocsis.com/rgplates/"
	cran = "rgplates" 

	version("0.4.0", md5="8307ba9d52c42829bf0623f191231eaa")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
