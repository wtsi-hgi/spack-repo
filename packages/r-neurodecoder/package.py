# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNeurodecoder(RPackage):
	"""Decode Information from Neural Activity

	Neural decoding is method of analyzing neural data that  
    uses a pattern classifiers to predict experimental conditions based 
    on neural activity. 'NeuroDecodeR' is a system of objects that 
    makes it easy to run neural decoding analyses. For more information
    on neural decoding see Meyers & Kreiman (2004)
    <doi:10.7551/mitpress/8404.003.0024>.
	"""
	
	homepage = "https://github.com/emeyers/NeuroDecodeR"
	cran = "NeuroDecodeR" 

	version("0.1.0", md5="236e89c70be01d7c8313697f769379f8")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-dosnow", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-r-matlab", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tictoc", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
