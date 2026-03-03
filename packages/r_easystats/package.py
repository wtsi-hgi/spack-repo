# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REasystats(RPackage):
	"""Framework for Easy Statistical Modeling, Visualization, and
Reporting

	A meta-package that installs and loads a set of packages from 
    'easystats' ecosystem in a single step. This collection of packages provide 
    a unifying and consistent framework for statistical modeling, visualization, 
    and reporting. Additionally, it provides articles targeted at instructors for 
    teaching 'easystats', and a dashboard targeted at new R users for easily 
    conducting statistical analysis by accessing summary results, model fit indices, 
    and visualizations with minimal programming.
	"""
	
	homepage = "https://easystats.github.io/easystats/"
	cran = "easystats" 

	version("0.7.1", md5="7b0a3a251614c9610c60d1b5a666d397")
	version("0.7.0", md5="4054a1cacb518b15ae300fca9501d208")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-bayestestr@0.13.2:", type=("build", "run"))
	depends_on("r-correlation@0.8.4:", type=("build", "run"))
	depends_on("r-datawizard@0.10:", type=("build", "run"))
	depends_on("r-effectsize@0.8.6:", type=("build", "run"))
	depends_on("r-insight@0.19.10:", type=("build", "run"))
	depends_on("r-modelbased@0.8.7:", type=("build", "run"))
	depends_on("r-parameters@0.21.6:", type=("build", "run"))
	depends_on("r-performance@0.11:", type=("build", "run"))
	depends_on("r-report@0.5.8:", type=("build", "run"))
	depends_on("r-see@0.8.3:", type=("build", "run"))
