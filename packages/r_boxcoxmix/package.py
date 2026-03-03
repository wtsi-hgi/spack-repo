# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBoxcoxmix(RPackage):
	"""Box-Cox-Type Transformations for Linear and Logistic Models with
Random Effects

	Box-Cox-type transformations for linear and logistic models with random effects using non-parametric profile maximum likelihood estimation, as introduced in Almohaimeed (2018) <http://etheses.dur.ac.uk/12831/> and Almohaimeed and Einbeck (2022) <doi:10.1177/1471082X20966919>. The main functions are 'optim.boxcox()' for linear models with random effects and 'boxcoxtype()' for logistic models with random effects.
	"""
	
	homepage = "https://gitlab.com/iagogv/boxcoxmix"
	cran = "boxcoxmix" 

	version("0.42", md5="dd8e7439e2c49f57e2531e6b3fb48c86")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-statmod@1.4.27:", type=("build", "run"))
	depends_on("r-qicharts@0.5.4:", type=("build", "run"))
	depends_on("r-npmlreg@0.46.1:", type=("build", "run"))
