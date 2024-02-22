# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLw1949(RPackage):
	"""An Automated Approach to Evaluating Dose-Effect Experiments
Following Litchfield and Wilcoxon (1949)

	The manual approach of Litchfield and Wilcoxon (1949)
    <http://jpet.aspetjournals.org/content/96/2/99.abstract>
    for evaluating dose-effect experiments
    is automated so that the computer can do the work. 
	"""
	
	homepage = "https://github.com/JVAdams/LW1949"
	cran = "LW1949" 

	version("1.1.0", md5="d62d48ff608906f1481f432e9232d0fa", url="https://cran.r-project.org/src/contrib/LW1949_1.1.0.tar.gz")

	depends_on("r@3.3.2:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-plotrix", type=("build", "run"))
