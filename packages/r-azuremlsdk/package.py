# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAzuremlsdk(RPackage):
	"""Interface to the 'Azure Machine Learning' 'SDK'

	Interface to the 'Azure Machine Learning' Software Development Kit
    ('SDK'). Data scientists can use the 'SDK' to train, deploy, automate, and
    manage machine learning models on the 'Azure Machine Learning' service. To
    learn more about 'Azure Machine Learning' visit the website:
    <https://docs.microsoft.com/en-us/azure/machine-learning/service/overview-what-is-azure-ml>.
	"""
	
	homepage = "https://github.com/azure/azureml-sdk-for-r"
	cran = "azuremlsdk" 

	version("1.10.0", md5="56abcf30669adc99694acaf0a4b4289d")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-reticulate@1.12:", type=("build", "run"))
	depends_on("r-plyr@1.8:", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-rstudioapi@0.7:", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-servr", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinycssloaders", type=("build", "run"))
