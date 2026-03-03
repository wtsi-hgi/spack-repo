# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROutlierensembles(RPackage):
	"""A Collection of Outlier Ensemble Algorithms

	Ensemble functions for outlier/anomaly detection. There is a new ensemble method proposed using 
    Item Response Theory. Existing outlier ensemble methods from Schubert et al (2012) <doi:10.1137/1.9781611972825.90>, 
    Chiang et al (2017) <doi:10.1016/j.jal.2016.12.002> and Aggarwal and Sathe (2015) <doi:10.1145/2830544.2830549>
    are also included.
	"""
	
	homepage = "https://sevvandi.github.io/outlierensembles/"
	cran = "outlierensembles" 

	version("0.1.0", md5="e89d2a8782d91ac1e576ed70f2c3a652")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-airt", type=("build", "run"))
	depends_on("r-estcrm", type=("build", "run"))
	depends_on("r-psych", type=("build", "run"))
	depends_on("r-apcluster", type=("build", "run"))
