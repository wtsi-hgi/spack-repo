# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRoi(RPackage):
	"""R Optimization Infrastructure

	The R Optimization Infrastructure ('ROI') <doi:10.18637/jss.v094.i15>
	is a sophisticated framework for handling optimization problems in R.
	Additional information can be found on the 'ROI' homepage <https://roi.r-forge.r-project.org/>.
	"""
	
	homepage = "https://roi.r-forge.r-project.org/"
	cran = "ROI" 

	version("1.0-1", md5="7c0e75cd514f58ca619ebb89b1a4750b")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-registry@0.5:", type=("build", "run"))
	depends_on("r-slam", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
