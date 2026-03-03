# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpinar(RPackage):
	"""(Semi)Parametric Estimation and Bootstrapping of INAR Models

	Semiparametric and parametric estimation of INAR models including a finite sample refinement (Faymonville et al. (2022) <doi:10.1007/s10260-022-00655-0>) for the semiparametric setting introduced in Drost et al. (2009) <doi:10.1111/j.1467-9868.2008.00687.x>, different procedures to bootstrap INAR data (Jentsch, C. and Weiß, C.H. (2017) <doi:10.3150/18-BEJ1057>) and flexible simulation of INAR data.
	"""
	
	homepage = "https://github.com/MFaymon/spINAR"
	cran = "spINAR" 

	version("0.1.0", md5="af3d8698d23e10446cb0007467ac468e")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-checkmate@1.8.5:", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
