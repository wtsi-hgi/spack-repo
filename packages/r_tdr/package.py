# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTdr(RPackage):
	"""Target Diagram

	Implementation of target diagrams using 'lattice' and 'ggplot2' graphics. Target diagrams provide a graphical overview of the respective contributions of the unbiased RMSE and MBE to the total RMSE (Jolliff, J. et al., 2009. "Summary Diagrams for Coupled Hydrodynamic-Ecosystem Model Skill Assessment." Journal of Marine Systems 76: 64–82.)
	"""
	
	homepage = "http://github.com/oscarperpinan/tdr"
	cran = "tdr" 

	version("0.13", md5="e94e59d167432ca8c63c0fce20d699dd")

	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
