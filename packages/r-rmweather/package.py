# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRmweather(RPackage):
	"""Tools to Conduct Meteorological Normalisation and Counterfactual
Modelling for Air Quality Data

	An integrated set of tools to allow data users to conduct 
    meteorological normalisation and counterfactual modelling for air quality 
    data. The meteorological normalisation technique uses predictive random 
    forest models to remove variation of pollutant concentrations so trends and 
    interventions can be explored in a robust way. For examples, see 
    Grange et al. (2018) <doi:10.5194/acp-18-6223-2018> and 
    Grange and Carslaw (2019) <doi:10.1016/j.scitotenv.2018.10.344>. The random
    forest models can also be used for counterfactual or business as usual (BAU) 
    modelling by using the models to predict, from the model's perspective, the 
    future. For an example, see Grange et al. (2021) <doi:10.5194/acp-2020-1171>.
	"""
	
	homepage = "https://github.com/skgrange/rmweather"
	cran = "rmweather" 

	version("0.2.5", md5="20b5a77b129c86edf22ad8eb440532fe")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-dplyr@1.0.1:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-pdp", type=("build", "run"))
	depends_on("r-purrr@1:", type=("build", "run"))
	depends_on("r-ranger", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-strucchange", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-viridis", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
