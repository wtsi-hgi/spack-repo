# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RH2otools(RPackage):
	"""Machine Learning Model Evaluation for 'h2o' Package

	Several functions are provided that simplify using 'h2o' 
             package. Currently, a function for extracting the AutoML 
             model parameter is provided, alongside a function for computing 
             F-Measure statistics at any given threshold. For more information 
             about 'h2o' package see <https://h2o.ai/>.
	"""
	
	homepage = "https://github.com/haghish/h2otools"
	cran = "h2otools" 

	version("0.3", md5="fbd1411a059ca5299f6c88ddae03f632")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-h2o@3.34:", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
