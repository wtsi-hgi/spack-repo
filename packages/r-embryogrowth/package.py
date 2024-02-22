# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REmbryogrowth(RPackage):
	"""Tools to Analyze the Thermal Reaction Norm of Embryo Growth

	Tools to analyze the embryo growth and the sexualisation thermal reaction norms. See <doi:10.7717/peerj.8451> for tsd functions; see <doi:10.1016/j.jtherbio.2014.08.005> for thermal reaction norm of embryo growth. 
	"""
	
	cran = "embryogrowth" 

	version("9.1", md5="20cb44b31d9d76342499235573c4e98a")

	depends_on("r-desolve", type=("build", "run"))
	depends_on("r-optimx", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-helpersmg@6.0.3:", type=("build", "run"))
	depends_on("r@4.1:", type=("build", "run"))
